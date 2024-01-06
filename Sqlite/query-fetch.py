import sqlite3

conn= sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT rowid, * FROM customers")
print(c.fetchall()) #print out all data in form a list

c.execute("SELECT  * FROM customers WHERE last_name='macharia'")
print(c.fetchall()) #print only details of customer whose lastname is macharia