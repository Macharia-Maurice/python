import sqlite3

conn= sqlite3.connect('customer.db')

c = conn.cursor()

#using other datafields
c.execute("""
          UPDATE customers SET first_name='mauricem'
          WHERE first_name='maurice'
    
""")

# using rowid

c.execute("""
          UPDATE customers SET first_name='maurice'
          WHERE rowid=1
          """)



conn.commit()
conn.close()

# better to use a rowid cause it is unique
