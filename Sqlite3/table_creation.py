import sqlite3

# establish a connection to our db
conn= sqlite3.connect('customer.db')

# create a cursor object from connection
c = conn.cursor() #cursor is used to execute sql commands


# execute a sql command to create a table
c.execute("""CREATE TABLE customers(
          first_name text,
          last_name text,
          email text
)
""")

conn.commit()
conn.close()