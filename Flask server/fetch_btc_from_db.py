import sqlite3

conn = sqlite3.connect('bitcoin_database.db')
cursor = conn.cursor()
rows = cursor.execute("SELECT * FROM bitcoin ORDER BY date DESC LIMIT 500")

for i in rows:
    print(i)