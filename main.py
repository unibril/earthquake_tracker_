from db import get_connection, initialize_db
from fetcher import fetch
initialize_db()
fetch()
