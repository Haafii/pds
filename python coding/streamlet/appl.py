from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Flask API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
