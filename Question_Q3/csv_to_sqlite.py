import csv
import sqlite3

connection = sqlite3.connect("Question_Q3/user.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
        )
    """)


with open("Question_Q3/users.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        email = row["email"]

        cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (?,?)
            """,
            (name, email)
        )

connection.commit() 
connection.close()

print("CSV data successfully inserted into SQLite.")