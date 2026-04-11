from db import get_connection, initialize_db
from fetcher import fetch
from analyzer import quake_by_month, quake_by_region, depth_vs_magnitude,tsunami
from visualizer import plot_quake_month, plot_quake_region, plot_tsunami, depth_magnitude
initialize_db()
fetch()
while True:
    option = input("Enter what you want to do 'quake by month' or 'depth vs magnitude' or 'quake by region' or anykey to exit")
    if option.lower().strip() =="quake by month":
        quake_by_month()
        plot_quake_month()
    elif option.lower().strip() =="quake by region":
        quake_by_region()
        plot_quake_region()
    elif option.lower().strip()=="tsunami":
        tsunami()
        plot_tsunami()
    elif option.lower().strip() == "depth vs magnitude":
        depth_vs_magnitude()
        depth_magnitude()
    else:
        break
   
