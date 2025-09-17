import sqlite3
import pandas as pd

def create_database():
    # Load Excel file and clean headers
    excel_file = "supermarkt_sales.xlsx"
    df = pd.read_excel(excel_file, header=2)  # Skip first 2 rows, use row 3 as header

    # Create SQLite database and insert clean data
    conn = sqlite3.connect("sales.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("Database created successfully with sales data!")

if __name__ == "__main__":
    create_database()
