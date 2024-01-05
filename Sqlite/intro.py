import sqlite3

# create a connection to our db

conn= sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customers(
          first_name DATATYPE,
          last_name DATATYPE,
          email DATATYPE

)

""")