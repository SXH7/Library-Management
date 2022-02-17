create database library;

use library;

create table member(Mem_ID char(4) NOT NULL PRIMARY KEY, 
                    Mem_Name varchar(30) NOT NULL, 
                    Mem_DOB date NOT NULL, 
                    Mem_Phone bigint(11) NOT NULL, 
                    Mem_address varchar(40) NOT NULL,
                    Mem_perms varchar(5) NOT NULL CHECK(Mem_perms = "Staff" or Mem_perms = "User"));



create table books(B_ID char(4) NOT NULL PRIMARY KEY,
                   B_Name varchar(30) NOT NULL,
                   B_Author varchar(30) NOT NULL,
                   B_Publisher varchar(20),
                   B_Avilable char(1) NOT NULL CHECK(B_Avilable = "Y" or B_Avilable = "N")),
                   B_Genre char(4) NOT NULL REFERENCES genre(Gen_ID);

create table issue(I_ID char(4) NOT NULL UNIQUE,
                   I_MemID char(4) REFERENCES member(Mem_ID),
                   I_Book char(4) REFERENCES books(B_ID),
                   I_Date date NOT NULL,
                   I_Due date NOT NULL);
