import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con = sqlt.connect(host = "localhost", user = "root", passwd = "Anuj@2830", database = "library" )
cursor = con.cursor()
def book_output():
    df = pd.read_sql("select * from book",con)
    print(tabulate(df, headers='keys', showindex='False', tablefmt='psql'))

def member_output():
    df = pd.read_sql("select * from member",con)
    print(tabulate(df, headers='keys', showindex='False', tablefmt='psql'))

def return_output():
    df = pd.read_sql("select * from returned",con)
    print(tabulate(df, headers='keys', showindex='False', tablefmt='psql'))

def issue_output():
    df = pd.read_sql("select * from issue",con)
    print(tabulate(df, headers='keys', showindex='False', tablefmt='psql'))



def col_chart():
    q = "select bookid, count(copies) as totalcopies from issue group by bookid;"
    df = pd.read_sql(q,con)
    print(df)
    plt.bar(df.bookid , df.totalcopies)
    plt.xlabel("Bookid")
    plt.ylabel("Copies issued")
    plt.title("Best reading book")
    plt.xticks(df.bookid)
    plt.show()