import sqlite3

conn=sqlite3.connect("customer.db")
c=conn.cursor()

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")