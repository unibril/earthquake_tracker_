# 🌍 Earthquake Tracker

A Python data pipeline that fetches real earthquake data from the USGS API, stores it in MySQL, and lets you analyze and visualize it interactively.

---

## What It Does

Fetches all earthquakes magnitude 4.5+ from 2024, stores them in a MySQL database, and lets you explore:

- **Quake by region** — top 10 most active locations
- **Quake by month** — how seismic activity varies across the year
- **Depth vs Magnitude** — scatter plot to spot correlations
- **Tsunami-linked quakes** — top 10 places with tsunami-triggering earthquakes

All charts render interactively via Plotly.

---

## Project Structure
earthquake_tracker/
├── main.py        # Entry point and CLI menu
├── fetcher.py     # Pulls data from USGS API and inserts into MySQL
├── analyzer.py    # Pandas-based analysis functions
├── visualizer.py  # Plotly chart functions
├── db.py          # MySQL connection and schema initialization
└── .gitignore

---

## Data Source

[USGS Earthquake Hazards Program API](https://earthquake.usgs.gov/fdsnws/event/1/)

- Range: January 2024 – December 2024
- Filter: Magnitude ≥ 4.5
- Format: GeoJSON

---

## Usage

```bash
python main.py
```

On first run it initializes the database and fetches data automatically. Then:
Enter what you want to do:
'quake by month' | 'quake by region' | 'depth vs magnitude' | 'tsunami' | any other key to exit

---

## Setup

### Prerequisites

- Python 3.8+
- MySQL running locally

### Install dependencies

```bash
pip install requests pandas plotly mysql-connector-python
```

### Configure database

In `db.py`, update your MySQL credentials:

```python
host="localhost"
user="your_user"
password="your_password"
database="earthquake_db"
```

Then run:

```bash
python main.py
```

The schema is created automatically on first run.

---

## Requirements
requests
pandas
plotly
mysql-connector-python

---

## About

Built using the USGS public earthquake API as part of a Python and data science portfolio.
