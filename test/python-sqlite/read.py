import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM numbers")

for row in cursor.fetchall():
    print(row)

conn.close()
