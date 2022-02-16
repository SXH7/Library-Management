create database library;

use library;

create table member(Mem_ID char(4) NOT NULL PRIMARY KEY, 
                    Mem_Name varchar(30) NOT NULL, 
                    Mem_DOB date NOT NULL, 
                    Mem_Phone int(11) NOT NULL, 
                    Mem_address varchar(40) NOT NULL,
                    Mem_perms varchar(5) NOT NULL CHECK(Mem_perms = "Staff" or Mem_perms = "User"));