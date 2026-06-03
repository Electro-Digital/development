import sqlite3

# Create or open database
conn = sqlite3.connect("mydatabase.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value INTEGER
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and table created successfully.")
