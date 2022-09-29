import sqlite3 as sql3
from os.path import exists

file_exists = exists('library.db')

def create_table():
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, topic TEXT, author TEXT)')
    conn.commit()
    conn.close()

def insert(topic, author):
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('INSERT INTO books (topic, author) VALUES(?, ?)',(topic, author))
    conn.commit()
    conn.close()

def view_all():
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def total_books():
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT SUM(*) FROM books')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id, topic, author):
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('UPDATE books SET topic=?, author=? WHERE id=?', (topic, author, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sql3.connect('library.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('DELETE FROM books WHERE id=?', (id))
    conn.commit()
    conn.close()

if file_exists:
    pass
else:
    create_table()
