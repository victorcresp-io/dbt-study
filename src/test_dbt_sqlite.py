import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

path_db = os.getenv("DB_PATH")
print(path_db)
conn =  sqlite3.connect(path_db)

cursor = conn.cursor()

'''res = cursor.execute("""
    SELECT *
    FROM sqlite_master
    WHERE type = 'view'
    AND name = 'staging_person'
""").fetchall()
'''
'''res = cursor.execute("SELECT * FROM data_age_dbt_study.csv").fetchall()
'''

res = cursor.execute("""
    SELECT name, type 
    FROM sqlite_master
    WHERE type IN ('table', 'view');
""").fetchall()


print(res)