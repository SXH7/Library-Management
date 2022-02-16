from asyncore import read
from pydoc import importfile
import mysql.connector as i

log=i.connect(host="localhost",user="root",password="shashwat",database="library_management_program")

def addbook():
    bn=input("Enter the book name:")
    c=input("Enter the book code:")
    t=input("Enter the total number of books:")
    s=input("Enter the subject of books:")
    data = (bn,c,t,s)
    sql='insert into book values(%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Book(s) Added sucessfully")
    print("------------------------------------------------------------------")

def issueb():
    ina=input("Enter name:")
    reg=input("Enter registration no.:")
    bco=input("Enter book code:")
    isu=input("Enter Date:")
    data=(ina,reg,bco,isu)
    sql='insert into issue values(%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Issue done sucessfully")
    print("------------------------------------------------------------------")
    bookup=(bco,-1)

def summitb():
    ina=input("Enter name:")
    reg=input("Enter registration no.:")
    bco=input("Enter book code:")
    isu=input("Enter Date:")
    data=(ina,reg,bco,isu)
    sql='insert into summit values(%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Submission done sucessfully")
    print("------------------------------------------------------------------")
    bookup=(bco,+1)
