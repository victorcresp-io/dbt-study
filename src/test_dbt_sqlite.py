import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

path_db = os.getenv("DB_PATH")
print(path_db)
conn =  sqlite3.connect(path_db)

cursor = conn.cursor()
res = cursor.execute("""
    SELECT *
    FROM sqlite_master
    WHERE type = 'view'
    AND name = 'staging_person'
""").fetchall()

'''res = cursor.execute("SELECT * FROM staging_person").fetchall()
'''
print(res)