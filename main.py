from asyncore import read
from pydoc import importfile
from select import select
import mysql.connector as i
from datetime import datetime

log=i.connect(host="localhost",user="root",password="remon",database="library")



def memberadd():
    mi=input("Enter member id given by admin:")
    
    n=input("Enter your name:")
    print("Enter the date in sequence of MM-DD-YYYY")
    d=(input("Enter the date:"))

    dat=datetime.strptime(d, '%m-%d-%Y')
    
    
    phno=int(input("Enter your phone no.:"))

    ader=input("Enter your address:")

    wr=input("Enter if you are a user or staff:")
    
    data=(mi,n,dat,phno,ader,wr)
    print(data)
    sql=("insert into member values (%s,%s,%s,%s,%s,%s)")
    c=log.cursor()
    c.execute(sql,data)
    log.commit()

    print("Member added successfully")

    

   
