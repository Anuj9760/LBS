import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate

con = sqlt.connect(host = "localhost", user = "root", passwd = "Anuj@2830", database = "library" )
cursor = con.cursor()
def issue_book():
    q = "select max(issueid) from issue;"
    cursor.execute(q)
    r = cursor.fetchone()[0]
    if r:
        issueid = r + 1
    else:
        issueid = 1
    x = int(input("Enter the memberid : "))
    q1 = "select * from member where memberid = {};".format(x)
    cursor.execute(q1)
    r = cursor.fetchone()

    if r:
        y = int(input("Enter the bookid : "))
        q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
        cursor.execute(q2)
        r = cursor.fetchone()

        if r:
            if r[1] > 0:
                issuedate = (input("Enter the issue date : "))
                copies = int(input("Enter the no. of copies : "))
                rem_copies = r[1] - copies
                q3 = "insert into issue values({},'{}',{},{},{});".format(issueid, issuedate, x, y, copies)
                cursor.execute(q3)
                r = cursor.fetchone()
                q4 = "update book set rem_copies = {} where bookid = {};".format(rem_copies,y)
                cursor.execute(q4)
                con.commit()
                print("\t\t\t\tBook issued ")
            else:
                print("\t\t\t\tBook is not Availaible")
        else:
            print("\t\t\t\tWrong book id")
    else:
        print("\t\t\t\tWrong memberid")

def return_book():
    q = "select max(returnid) from returned;"
    cursor.execute(q)
    r = cursor.fetchone()[0]
    if r:
        returnid = r + 1
    else:
        returnid = 1
    x = int(input("Enter the memberid : "))
    q1 = "select * from member where memberid = {};".format(x)
    cursor.execute(q1)
    r = cursor.fetchone()

    if r:
        y = int(input("Enter the bookid : "))
        q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
        cursor.execute(q2)
        r = cursor.fetchone()

        if r:
        
            returndate = (input("Enter the return date : "))
            copies = int(input("Enter the no. of copies : "))
            rem_copies = r[1] + copies
            q3 = "insert into returned values({},'{}',{},{},{});".format(returnid, returndate, x, y, copies)
            cursor.execute(q3)
            r = cursor.fetchone()
            q4 = "update book set rem_copies = {} where bookid = {};".format(rem_copies,y)
            cursor.execute(q4)
            con.commit()
            print("\t\t\t\tBook returned succesfully ")
            
        else:
            print("\t\t\t\tWrong book id")
    else:
        print("\t\t\t\tWrong memberid")