import sqlite3

conn= sqlite3.connect('customer.db')

c = conn.cursor()

many_customers=[
    ('john', 'doe', 'doe@gmail.com'),
    ('munich', 'bayern' ,'bayern@gmail.com'),
    ('real', 'madrid', 'madrid@gmail.com')
]

c.executemany("INSERT INTO customers VALUES(?, ?, ?)",many_customers)

conn.commit()

conn.close()
