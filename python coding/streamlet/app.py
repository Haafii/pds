from flask import Flask, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load Excel file (replace with your Excel file path)
EXCEL_FILE = "sales_data.xlsx"

# Endpoint: read data from Excel
@app.route("/api/excel_data", methods=["GET"])
def get_excel_data():
    df = pd.read_excel(EXCEL_FILE)
    return jsonify(df.to_dict(orient="records"))

# Endpoint: read data from SQLite
@app.route("/api/sql_data", methods=["GET"])
def get_sql_data():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return jsonify(df.to_dict(orient="records"))

# Endpoint: aggregated sales (for charts)
@app.route("/api/sales_summary", methods=["GET"])
def get_sales_summary():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    summary = df.groupby("product")["quantity"].sum().reset_index()
    return jsonify(summary.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
