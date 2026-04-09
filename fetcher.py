import requests 
from db import get_connection, initialize_db
from datetime import datetime, timezone


def fetch():
    conn = get_connection()
    cursor = conn.cursor()
    
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2024-01-01&endtime=2024-12-31&minmagnitude=4.5"
    response = requests.get(url)
    data = response.json()

    for me in data["features"]: 
        magnitude = me["properties"]["mag"]
        place = me["properties"]["place"]
        depth = me["geometry"]["coordinates"][2]
        id_ = me["id"]
        latitude = me["geometry"]["coordinates"][1]
        longitude = me["geometry"]["coordinates"][0]
        time = me["properties"]["time"]
        tsunami = me["properties"]["tsunami"]

        made_time = datetime.fromtimestamp(time / 1000, tz=timezone.utc)

        cursor.execute("INSERT IGNORE INTO earthquakes (id, magnitude, place, time, depth, latitude, longitude, tsunami )VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(id_, magnitude, place,made_time, depth,latitude, longitude, tsunami))
    conn.commit()
    cursor.close()
    conn.close()
