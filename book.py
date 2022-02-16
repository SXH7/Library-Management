from aiohttp import BasicAuth
import mysql.connector as i

log=i.connect(host="localhost",user="root",password="remon",database="library")

def viewbook():

    c=log.cursor()
    c.execute("select * from books")
    result= c.fetchall()
    for row in result:
        print(row)
        print("\n")

def addbook():
    bid=input("Enter the book ID:")
    bnm=input("Enter the book name:")
    bauth=input("Enter the name book's author:")
    bpub=input("Enter the book's publisher:")
    bsts=input("If available or not:")
    data = (bid,bnm,bauth,bpub,bsts)
    sql='insert into books values(%s,%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Book(s) Added sucessfully")
