from Backend.book import *
from Backend.issue import *
from Backend.member import *

def main():
    print("1. Enter Book menu(1)")
    print("2. Enter Member menu(2)")
    print("3. Enter Issue menu(3)")
    print("4. Exit(4)")

    res=input("Enter your response here:")


    if res == '1' :
        bookm()
    elif res=='2' :
        memmen()
    elif res== '3' :
        ishmen()
    elif res=='4':
        exit()
    else:
        print("Invalid input")
        main()



def bookm():
    print("To view books(1):")
    print("To add book(2):")
    
    
    an=input("Enter your response here:")

    if an=='1':
        print("The book details are in order of (Book ID, Book name, Book Author,Book publisher,Avilable(yes/no))")
        viewbook()
        main()
    elif an=='2':
        print("--------------------You are in Add Book menu--------------------")
        addbook()
        main()
    else:
        print("Invalid input")
        main()

def ishmen():
    print("View issue database(1):")
    print("Issue a book")
    an=input("Enter your response here:")

    if an=='1':
        print("The Issue details are in order of (Issue ID,Member ID,book code,Issue date,Due date")
        viewbook()
        main()
    elif an=='2':
        print("--------------------You are in Create Issue menu--------------------")
        addbook()
        main()
    else:
        print("Invalid input")
        main()
def memmen():
    print("View Member database(1):")
    print("Add a member(2)")
    an=input("Enter your response here:")

    if an=='1':
        print("The Member details are in order of (Member ID,Member name,DOB,Address,Status")
        viewmemb()
        main()
    elif an=='2':
        print("--------------------You are in Add Member menu--------------------")
        memberadd()
        main()
    else:
        print("Invalid input")
        main()
main()