import sqlite3 as sql3
from os.path import exists

file_exists = exists('genesis.db')

def create_table():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('CREATE TABLE IF NOT EXISTS customers_order (id INTEGER PRIMARY KEY, name TEXT, pizza TEXT, pepperoni TEXT, cheese TEXT, price REAL)')
    conn.commit()
    conn.close()

def insert(name, pizza, pepperoni, chesse, price):
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('INSERT INTO customers_order (name, pizza, pepperoni, cheese, price) VALUES(?, ?, ?, ?, ?)',(name, pizza, pepperoni, chesse, price))
    conn.commit()
    conn.close()

def view_all():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT * FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def total_price():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT SUM(price) FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def max_price():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT MAX(price) FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def min_price():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT MIN(price) FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def avg_price():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT AVG(price) FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def count_order():
    conn = sql3.connect('genesis.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('SELECT COUNT(*) FROM customers_order')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

if file_exists:
    pass
else:
    create_table()
