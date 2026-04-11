from db import get_connection, initialize_db 
import pandas as pd 
import plotly as plt

def load_data():
    conn = get_connection()
    equake = pd.read_sql("SELECT * FROM earthquakes", conn)
    return equake

def quake_by_region():
    df =load_data()
    no_of_quake = df['place'].value_counts().head(10)
    return no_of_quake 

def depth_vs_magnitude():
    df = load_data()
    return df[["depth", "magnitude"]]

def quake_by_month():
    df = load_data()
    quakes_in_month = df['time'].dt.month.value_counts().sort_index()
    return quakes_in_month

def tsunami():
    df = load_data()
    filtered = df[df['tsunami']==1]
    k_bolxa = filtered['place'].value_counts().head(10)
    return k_bolxa