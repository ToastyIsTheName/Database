#This program will make my database
#The database being created is for my NEA Prototype Program

#This imports sqlite3, linking python and the database program.
import sqlite3
#This creates the database and titles it " "
db = sqlite3.connect("neapp.db")
#This creates a table and labels all of the rows inside the table
sql1 = "CREATE TABLE IF NOT EXISTS Tickets (Ticket_ID TEXT NOT NULL PRIMARY KEY, \
    Purchase_Date TEXT NOT NULL, Duration TEXT NOT NULL, \
    Valid_Until TEXT NOT NULL, Fee_Paid INT NOT NULL)"
#This executes the creation of the table
db.execute(sql1)

db.commit()
#This is a message so that if something does not print I will know around what area the issue is, making debugging much easier
print("The tickets table has been created succesfully ")

sql2 = "CREATE TABLE IF NOT EXISTS Vehicle (Vehicle_Reg TEXT NOT NULL PRIMARY KEY, \
    Vehicle_Make TEXT NOT NULL, Vehicle_Colour TEXT NOT NULL, \
    Vehicle_Body TEXT NOT NULL)"

db.execute(sql2)
db.commit()
print("The Vehicle table has been created succesfully ")

sql3 = "CREATE TABLE IF NOT EXISTS Customer (Customer_ID TEXT NOT NULL PRIMARY KEY, \
    First_Name TEXT NOT NULL, Last_Name TEXT NOT NULL, \
    Gender TEXT NOT NULL, DOB TEXT NOT NULL)"

db.execute(sql3)
db.commit()
print("The Customer table has been created succesfully ")

sql4 = "CREATE TABLE IF NOT EXISTS Branch (Branch_ID TEXT NOT NULL PRIMARY KEY, \
    Address_1 TEXT NOT NULL, Address_2 TEXT NOT NULL, \
    Postcode TEXT NOT NULL, Capacity TEXT NOT NULL, \
    Num_Of_Vehicles TEXT NOT NULL)"

db.execute(sql4)
db.commit()
print("The branch table has been created succesfully ")

choice = input("Press any key to continue ")

    
