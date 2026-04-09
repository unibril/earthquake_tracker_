import mysql.connector
import os 
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def initialize_db():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS earthquake_db")
    cursor.execute("USE earthquake_db")

    cursor.execute("""CREATE TABLE IF NOT EXISTS earthquakes (
            id VARCHAR(20) PRIMARY KEY,
            magnitude FLOAT,
            place VARCHAR(255),
            time DATETIME,
            depth FLOAT,
            latitude FLOAT,
            longitude FLOAT,
            tsunami INT)"""
                   )

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized.")