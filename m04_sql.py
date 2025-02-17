import sqlalchemy as sa

# Create a connection to books.db
engine = sa.create_engine("sqlite:///books.db")
conn = engine.connect()

# Query to select the title column in alphabetical order
sql = sa.text("SELECT title FROM books ORDER BY title;")
rows = conn.execute(sql)

# Print each title
for row in rows:
    print("Title:", row[0])

# Close the connection
conn.close()
engine.dispose()
