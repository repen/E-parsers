'''
MIT License https://github.com/repen/E-parsers/blob/master/License
'''

import sqlite3
import csv
def create_table():
    conn = sqlite3.connect("work.db")
    sql = "CREATE TABLE work (code TEXT, documentid TEXT)"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()

def insert_table(args):
    conn = sqlite3.connect("work.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO work VALUES(?,?)", args)
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect("work.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM work")
    res = cursor.fetchall()
    conn.close()
    return res
# create_table()
# for data in get_data():
#     code = data[0]
#     docid = data[1]
#     print(code, docid)

'sad'.r
for x in range(10):
    insert_table([("x", "x")])


# conn = sqlite3.connect("mydata.db")
# cursor = conn.cursor()

# sql = "CREATE TABLE books (name TEXT, price TEXT, description TEXT, info TEXT)"
# sql = "SELECT * FROM books"
# cursor.execute(sql)
# res = cursor.fetchall()
# print(res)
# sql = "INSERT INTO books VALUES (?, ?, ?, ?)"
