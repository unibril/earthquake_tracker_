from db import get_connection, initialize_db 
import pandas as pd 

def load_data():
    conn = get_connection()
    equake = pd.read_sql("SELECT * FROM earthquakes", conn)
    return equake

def quake_by_region():
    df =load_data()
    no_of_quake = df['place'].value_counts().head(10)
    return no_of_quake 



