import fastapi
import sqlite3

db = sqlite3.connect("DnDB.db")


endpoint = fastapi()

@endpoint.get("/")
async def root():
    return {'field':'This is a test field', 
            'non-string field':3.1415}