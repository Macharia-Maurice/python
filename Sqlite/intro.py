import sqlite3

# establish a connection to our db
conn= sqlite3.connect('customer.db')

# create a cursor object from connection
c = conn.cursor() #cursor is used to execute sql commands

c.execute("SELECT  * FROM customers")
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

#commit changes
conn.commit()

#close connection(optional)
conn.close()