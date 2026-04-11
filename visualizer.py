from analyzer import depth_vs_magnitude, quake_by_month,quake_by_region,tsunami
import plotly.express as px

def plot_quake_region():
    huh = quake_by_region()
    
    fig = px.bar(huh, x = huh.index, y = huh.values)
    fig.show()
def plot_quake_month():
    huh = quake_by_month()
    fig = px.bar(huh,x = huh.index, y = huh.values)
    fig.show()

def depth_magnitude():
    huh = depth_vs_magnitude()
    fig = px.scatter(huh, x =huh.depth , y = huh.magnitude)
    fig.show()

def plot_tsunami():
    huh = tsunami()
    fig = px.bar(huh, x = huh.index, y = huh.values)
    fig.show()