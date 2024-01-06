import sqlite3

conn=sqlite3.connect('customer.db')
c=conn.cursor()

c.execute("select * from customers limit 2")
print()
