from flask import Flask,jsonify,request
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

app = Flask(__name__)

def read_excel_data():
    df = pd.read_excel('supermarkt_sales.xlsx')
    return df

def read_sql_data():
    engine = create_engine('sqlite:///sales.db')
    df = pd.read_sql('SELECT * FROM sales',con=engine)
    return df

def convert_time_columns_to_str(df):
    for col in df.columns:
        if df[col].dtype == 'object' and df[col].apply(lambda x: hasattr(x, 'isoformat')).any():
            df[col] = df[col].apply(lambda x: x.isoformat() if hasattr(x, 'isoformat') else x)
    return df

@app.route('/api/xlsx',methods=['GET'])
def get_excel_data():
    df = read_excel_data()
    df = convert_time_columns_to_str(df)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/sql',methods=['GET'])
def get_sql_data():
    df = read_sql_data()
    df = convert_time_columns_to_str(df)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/sales',methods=['GET'])
def get_sales_data():
    source = request.args.get('source','excel')
    if source == 'excel':
        df = read_excel_data()
    else:
        df = read_sql_data()

    product = request.args.get('product')
    if product:
        df = df[df['Product']==product]

    df = convert_time_columns_to_str(df)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)