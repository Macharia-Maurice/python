import sqlite3

conn=sqlite3.connect('customer.db')
c=conn.cursor()

def show_all():
    c.execute("select rowid,* from customers ")

    persons=c.fetchall()
    for person in persons:
        print(person)

    conn.close()

def add_one_record(first_name,last_name,email):
    c.execute("insert into customers values(?,?,?)",(first_name,last_name,email))
    conn.commit()

def delete_record(rowid):
    c.execute("delete from customers where rowid=(?)",(rowid,)) #pass parameters as a tuple
    conn.commit()

def add_many_records(list):
    c.executemany("insert into customers values(?,?,?)",(list))
    conn.commit()

def search_by_id(id):
    c.execute("select * from customers where rowid=(?)", (id,))
    return c.fetchall()