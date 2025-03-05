import sqlite3
import csv

def importCSV():
    # Convert the CSV string to a file-like object
    csv_file = open('content/netflix_titles.csv', 'r')

    # Connect to SQLite database and create it even if it exist
    conn = sqlite3.connect('netflix_titles.db')
    cursor = conn.cursor()

    # Create a table to store the data
    cursor.execute('''
    CREATE TABLE titles  (
        show_id TEXT,
        type TEXT,
        title TEXT,
        director TEXT,
        cast_in TEXT,
        country TEXT,
        date_added TEXT,
        release_year INTEGER,
        rating TEXT,
        duration TEXT,
        listed_in TEXT,
        description TEXT
    )
    ''')

    # Read the CSV data and insert into the SQLite table
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Clean up the data (remove trailing semicolons and strip whitespace)
        cursor.execute('''
          INSERT INTO titles (show_id, type, title, director, cast_in, country, date_added, release_year, rating, duration, listed_in, description)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
        ''', row)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print("Data imported successfully!")

if __name__ == '__main__':
    importCSV()