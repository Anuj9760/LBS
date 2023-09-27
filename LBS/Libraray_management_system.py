import books
import members
import Transaction
import Report

#---------------------Library Management System----------------------------------
while(True):
    print("="*100)
    print("\t\t\t\tLibrary Management System")
    print("="*100)
    print("\t\t\t\tEnter the choice\n \t\t\t\t1. Book Details \n \t\t\t\t2. Member details \n \t\t\t\t3. Transactions \n \t\t\t\t4. Report \n \t\t\t\t5. Exit")
    choice = int(input())
    if choice == 1:
        while(True):
            print("\t\t\t\tEnter the choice\n \t\t\t\t1.Add new Book \n \t\t\t\t2.Edit Book Details \n \t\t\t\t3.Delete a Book \n \t\t\t\t4.Search a Book \n \t\t\t\t5.Back to the Main Menu")
            bookchoice = int(input())
            if bookchoice == 1:
                books.book_input()
            elif bookchoice == 2:
                books.edit_input()
            elif bookchoice == 3:
                books.delete_book()
            elif bookchoice == 4:
                books.search_book()
            elif bookchoice == 5:
                break

    elif choice == 2:
        while(True):
            print("\t\t\t\tEnter the choice \n \t\t\t\t1.Add new Member \n \t\t\t\t2.Edit Member Details \n \t\t\t\t3.Delete Member \n \t\t\t\t4.Search Member \n \t\t\t\t5.Back to the Main Menu")
            memberchoice = int(input())
        
            if memberchoice == 1:
                members.member_input()
            elif memberchoice == 2:
                members.member_edit_input()
            elif memberchoice == 3:
                members.delete_member()
            elif memberchoice == 4:
                members.search_member()
            elif memberchoice == 5:
                break
    elif choice == 3:
        while(True):
            print("\t\t\t\tEnter the choice \n \t\t\t\t1.Issue A Book \n \t\t\t\t2.Return A Book \n \t\t\t\t3.Back to the Main Menu")
            Trasactionchoice = int(input())
        
            if Trasactionchoice == 1:
                Transaction.issue_book()
            elif Trasactionchoice == 2:
                Transaction.return_book()
            elif Trasactionchoice == 3:
                break
    elif choice == 4:
        while(True):
            print("\t\t\t\tEnter the choice \n \t\t\t\t1.Book Details \n \t\t\t\t2.Member Details \n \t\t\t\t3.Issue Details \n \t\t\t\t4.Return Details \n \t\t\t\t5.Best Reading Book(Chart) \n \t\t\t\t6.Back to the Main Menu")
            reportchoice = int(input())
        
            if reportchoice == 1:
                Report.book_output()
            elif reportchoice == 2:
                Report.member_output()
            elif reportchoice == 3:
                Report.issue_output()
            elif reportchoice == 4:
                Report.return_output()
            elif reportchoice == 5:
                Report.col_chart()
            elif reportchoice == 6:
                break
    elif choice == 5:
        break
