# # Create & Connect to a database
# # Create a cursor object
# # Write an SQL query
# # Commit changes 
# # Close database connection
# # 

import sqlite3 as sql3

# conn = sql3.connect('library_test.db') # Create the db 
# cursor = conn.cursor() # Create a cursor
# cursor.execute('CREATE TABLE IF NOT EXISTS books (id PRIMARY KEY INTEGER title TEXT, author TEXT)')
# cursor.execute('INSERT INTO books (title, author) VALUES("The Alphabet","Emmy Kelly")')
# conn.commit()
# conn.close()

def create_table():
    conn = sql3.connect('library_test.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')
    conn.commit()
    conn.close()

def insert(title, author):
    conn = sql3.connect('library_test.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('INSERT INTO books (title, author) VALUES(?, ?)',(title, author))
    conn.commit()
    conn.close()

def view_all():
    conn = sql3.connect('library_test.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sql3.connect('library_test.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('DELETE FROM books WHERE id=?', (id))
    conn.commit()
    conn.close()


def update(id, title, author):
    conn = sql3.connect('library_test.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('UPDATE books SET title=?, author=? WHERE id=?', (title, author, id))
    conn.commit()
    conn.close()

update(2, 'Python For Intermediate', 'Kevwe Sophia')

print(view_all())