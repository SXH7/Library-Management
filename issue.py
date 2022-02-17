import mysql.connector as i
from datetime import datetime

log=i.connect(host="localhost",user="root",password="remon",database="library")

def viewissues():

    c=log.cursor()
    c.execute("select * from issue")
    result= c.fetchall()
    for row in result:
        print(row)
        print("\n")

def issuebook():
    iid=input("Enter issue ID:")
    mmid=input("Enter member id:")
    bc=input("Enter the book code:")
    
    
    B=(bc,)

    


    c=log.cursor()
    sql=("select B_Avilable from books where B_ID=%s")
    c.execute(sql,B)
    res=c.fetchall()

    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1

    
    if 'Y' in res[0]:
        adate=input("Enter book issue date (MM-DD-YYYY):")
        bdate=input("Enter due date(MM-DD-YYYY):")
        idate=datetime.strptime(adate, '%m-%d-%Y')
        duedate=datetime.strptime(bdate, '%m-%d-%Y')
        
        data=(iid,mmid,bc,idate,duedate)
        sq=("insert into issue values(%s,%s,%s,%s,%s)")
        
        c=log.cursor()
        c.execute(sq,data)
        log.commit()
        print("Book issued successfully!")
    else:
        print("Either book isnt avilable or code is wronge:")
        issuebook()

viewissues()
    
        













issuebook()