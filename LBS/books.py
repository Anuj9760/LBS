import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate

con = sqlt.connect(host = "localhost", user = "root", passwd = "Anuj@2830", database = "library" )
cursor = con.cursor()
def book_input():
    try:
        bookid = input("Enter bookid : ")
        bname = input("Enter the Book name : ")
        author = input("Enter the name of author : ") 
        price = float(input("Enter the price : "))
        copies = int(input("Enter the no. of copies : "))
        qry = "insert into book values({},'{}','{}',{},{},{});".format(bookid,bname,author,price,copies,copies)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tbook added succesfully")
    except:
        print("Error.... Wrong Entry")

def edit_input():
    x = int(input("Enter book id : "))
    qry = "select * from book where bookid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        y = float(input("Enter the new price : "))
        qry = "update book set price ={} where bookid = {};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tEdit succesfully")
    else:
        print("\t\t\t\tWrong book id")

def delete_book():
    x = int(input("Enter book id : "))
    qry = "select * from book where bookid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        qry = "delete from book where bookid = {};".format(x)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tdeleted succesfully")
    else:
        print("\t\t\t\tWrong book id")

def search_book():
    x = int(input("Enter book id : "))
    qry = "select * from book where bookid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df, tablefmt='psql', showindex='False', headers='keys'))
    else:
        print("\t\t\t\tWrong book id")
