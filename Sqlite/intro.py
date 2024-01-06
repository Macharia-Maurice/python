import sqlite3

# establish a connection to our db
conn= sqlite3.connect('customer.db')

# create a cursor object from connection
c = conn.cursor() #cursor is used to execute sql commands
# c.execute("""
#           UPDATE customers SET first_name='mauricem'
#           WHERE first_name='maurice'
    
# """)
# c.execute("""
#           UPDATE customers SET first_name='maurice'
#           WHERE rowid=1
#           """)

# c.execute("""
#             UPDATE customers SET email='maurice@yahoo.com'
#           WHERE rowid=2
# """)
#commit changes
# c.execute("INSERT INTO customers VALUES('jane', 'downsbrery', 'jane@gmail.com')")

# c.execute("DELETE from customers WHERE rowid=2")

# conn.commit()


c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
# c.execute("select rowid, * from customers order by rowid desc")
# c.execute("SELECT  rowid, * FROM customers")
# rowid - primary key
# print(c.fetchone()[2])
# print(c.fetchmany(2))

items=c.fetchall()
for item in items:
    print(item)

# # execute a sql command to create a table
# c.execute("""CREATE TABLE customers(
#           first_name text,
#           last_name text,
#           email text
# )
# """)

# many_customers=[
#     ('john', 'doe', 'doe@gmail.com'),
#     ('munich', 'bayern' ,'bayern@gmail.com'),
#     ('real', 'madrid', 'madrid@gmail.com')
# ]

# c.executemany("INSERT INTO customers VALUES(?, ?, ?)",many_customers)

# c.execute("INSERT INTO customers VALUES('maurice', 'maina', 'maina@gmail.com')")

conn.commit()

#close connection(optional)
conn.close()