import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO numbers (value) VALUES (?)", (100,))
cursor.execute("INSERT INTO numbers (value) VALUES (?)", (200,))

conn.commit()
conn.close()
