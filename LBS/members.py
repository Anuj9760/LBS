import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate

con = sqlt.connect(host = "localhost", user = "root", passwd = "Anuj@2830", database = "library" )
cursor = con.cursor()
def member_input():
    try:
        memberid = input("Enter memberid :")
        mname = input("Enter the Member name :")
        madd = input("Enter the Address :") 
        phone = (input("Enter the phone number :"))
        qry = "insert into member values({},'{}','{}','{}');".format(memberid,mname,madd,phone)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tmember added succesfully")
    except:
        print("Error.... Wrong Entry")

def member_edit_input():
    x = int(input("Enter member id :"))
    qry = "select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        y = (input("Enter the new Address :"))
        qry = "update member set madd = '{}' where memberid = {};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tEdit succesfully")
    else:
        print("\t\t\t\tWrong member id")

def delete_member():
    x = int(input("Enter member id :"))
    qry = "select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        qry = "delete from member where memberid = {};".format(x)
        cursor.execute(qry)
        con.commit()
        print("\t\t\t\tdeleted succesfully")
    else:
        print("\t\t\t\tWrong member id")

def search_member():
    x = int(input("Enter member id :"))
    qry = "select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df, tablefmt='psql', showindex='False', headers='keys'))
    else:
        print("\t\t\t\tWrong member id")