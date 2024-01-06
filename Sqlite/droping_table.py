import sqlite3

conn=sqlite3.connect('customer.db')
c=conn.cursor()

c.execute("drop table customers")
conn.commit()