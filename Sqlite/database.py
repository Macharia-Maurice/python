import sqlite3


def show_all():
    conn=sqlite3.connect('customer.db')
    c=conn.cursor()

    c.execute("select rowid,* from customers ")
    persons=c.fetchall()

    for person in persons:
        print(person)

    conn.close()

show_all()


# c.execute("select rowid,* from customers ")
# print(c.fetchall())