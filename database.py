import sqlite3
import csv
from sqlite3 import Error

def sqlconnection():
    try:
        con = sqlite3.connect(':memory:')
        print('ok')
        return con
    except:
        print('error')
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('Create table details(id integer PRIMARY KEY,date blob,company blob,fundtype blob)')
    print('done')
    con.commit()
    cursorObj.execute('SELECT * FROM details;')
def insertion(con):
    cursor= con.cursor()
    with open ('sample.csv') as f:
        csv_reader= csv.reader(f)
        a=[]
        for i in csv_reader:
            a.append(i)
        for i in a:
            cursor.execute('insert into details values (?,?,?,?)',i)
            con.commit()
        statement='''select * from details'''
        cursor.execute(statement)
        output=cursor.fetchall()
        for row in output:
            print(row)
con=sqlconnection()
sql_table(con)
insertion(con)