import requests
import sqlite3

API_URL ="https://openlibrary.org/search.json?q=python"

response = requests.get(API_URL, timeout=10)
response.raise_for_status()

data = response.json()

books = data["docs"][:10]

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        publication_year INTEGER,
        UNIQUE(title, author, publication_year)
    )
""")

for book in books:

    title = book.get("title", "Unknown")

    authors = book.get("author_name", [])
    author = authors[0] if authors else "Unknown"

    publication_year = book.get("first_publish_year")

    cursor.execute(
         """
        INSERT OR IGNORE INTO books (title, author, publication_year)
        VALUES (?,?,?)
        """,
        (title, author, publication_year)
    )

connection.commit()

cursor.execute("""
    SELECT id, title, author, publication_year
    FROM books
""")

rows = cursor.fetchall()

print("\nBooks stored in SQLite: ")
print("_" * 70)

for row in rows:
    book_id, title, author, publication_year = row

    print(
        f"{book_id}. {title} |"
        f"{author} |"
        f"{publication_year}"
    )

connection.close()
