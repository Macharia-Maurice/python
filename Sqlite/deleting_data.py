import sqlite3

conn= sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("DELETE from customers WHERE rowid=1")

conn.commit()
conn.close()
