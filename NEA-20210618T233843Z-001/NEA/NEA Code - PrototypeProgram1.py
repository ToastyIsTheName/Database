#Ollie W-B
#Prototype Program
#When the final program is started this will be used as infastructre and a testing program before moving things to the live program


#imports time so I can add natural pauses between outputs. Makes it seem more human
import time
#Connects Python to SQL so the database can work
import sqlite3
#Imports random
import random
#Imports sys so that people can exit the menu should they want to
import sys
#Imports the banner file I created so the companys software is 'watermarked'
from Banner1 import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         TO DO                                ||
#Customer Menu - Only used for testing so far                  ||
#Add more time/pauses. Make program seem more human            ||
#Ticket Menu - Timestamps - Calculating funds ETC              ||
#                                                              ||
#                                                              ||                                                                           
#                                                              ||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Creates Start Menu which will be the "Reception" of the system
def start_menu():
    banner()
    print(" ")
    choice = input("Welcome to Tozo Motorstop! Would you like to Register(R), Login(L) or Exit(E)? ")
#It is non caps sensitive to avoid user and software clashes
    if choice == "R" or choice =="r":
        register()
    elif choice =="L" or choice == "l":
        login()
    elif choice =="E" or choice == "e":
        sys.exit()
    else:
        start_menu()

#This block is creating the register function so users can make an account


#The Register menu will include more questions to gain extra data but I didn't think the prototype needed the extra detail yet.        
def register():
#This generates a random 2 digit number
    number = random.randint(10,99)
    level = "user"
#Username1 = Takes their desired username and adds the generated 2 digit number on
    username1 = input("Please enter your desired username: ")
    username = username1+str(number)
#This prints the final product of the sum
#The time will make it seem more human and less bunched together
    time.sleep(1)
    print("Your username is %s " % username)
    password = input("Enter a password for your account: ")
#This logs the username and password into the database
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        userdata = [username, password, level]
        sql = "insert into User_Data(Username, Password, Level) values (?,?,?)"
        cursor.execute(sql,userdata)
        db.commit()
        print("Your data has been added to our system ")
#Once registered it runs back to the menu so they have the choice to login
    start_menu()


#This is creating the login function for users to use their created accounts
def login():
#inputname being global means we can use it to find the users data easier in other sections of the code
    global inputname
    inputname = input("Please enter your username ")
#This is selecting the usernames from the saved accounts to see if the inputted username matches any
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT Username FROM User_Data WHERE Username = '%s'" %inputname)
        name = str(cursor.fetchone())
        username = name.strip(" (),' ")

    if inputname ==username:
        print("Your username has been recognised ")
        inputpwd = input("Please input your password ")
#This is selecting the passwords from the saved accounts to see if the inputted password matches any
        cursor.execute(" SELECT password FROM User_Data WHERE Username = '%s'" %inputname)
        password = str(cursor.fetchone())
        password = password.strip(" (),' ")


        if inputpwd == password:
            print("Your password has been recognised ")
            cursor.execute(" SELECT level FROM User_Data WHERE Username = '%s'" %inputname)
            level = str(cursor.fetchone())
            level = level.strip(" (),' ")
            print("Your access level is %s" %level)
#This checks if you hold the User, Administrator or Management role to understand what menus you can view.
            if level == "Administrator":
                admin_menu()
            else:
                print("You do not have access to the administrator menu ")
        else:
            print("The password you have entered doesn't match the given username. Please try again ")
            login()
    else:
        print("The username you have inputted has not been recognised. Please try again ")
        login()
            
            


#This is the Administration Menu. It will be for the basic level of staff access....
#The menu will give permissions to edit, add data ETC using SQL scripts
#NOTES#######
#Choice1 = view data "menu"
#choice 2 = edit data "menu"
#Choice 3 = Exit to a menu (customer) maybe
def admin_menu():
    print(" ")
    time.sleep(0.5)
    print("Welcome to the Administrator Menu ")
    time.sleep(1)
    choice = input("Would you like to view data? ")
    if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
        viewdata()
    elif choice =="No" or choice =="no" or choice =="n" or choice =="N":
        choice1 = input("Would you like to exit to the Start Menu? ")
        if choice1 =="Yes" or choice1 =="yes" or choice1 =="y" or choice1 =="Y":
            start_menu()
        elif choice1 == "No" or choice1 == "no" or choice1 == "N" or choice1 == "n":
            choice2 = input("Would you like to exit to the Customer Menu? ")
            if choice2 =="Yes" or choice2 =="yes" or choice2 =="y" or choice2 =="Y":
                customer()
        elif choice2 == "No" or choice2 == "no" or choice2 == "N" or choice2 == "n":
            sys.exit()
                
    else:
        admin_menu()


#Here you choose what data you would like to view
def viewdata():
    print("You have chose to view data")
    choice = input("Would you like to view Customer, Your data(MD) or Exit ? ")
    if choice == "Customer" or choice == "customer" or choice == "C" or choice == "c":
        viewcustomer()
    elif choice == "MD" or choice == "md":
        md()
    else:
        start_menu()
        
#This will print the entirety of the Customer Data in the Customer Table.
def viewcustomer():
    print("You have chosen to view Customer data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer")
        vc = cursor.fetchall()
        for x in vc:
            print(vc)
        else:
            time.sleep(5)
            admin_menu()


#Global inputname allows us to view the inputted usernames data
def md():
    print("You have chosen to view your data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        myd = cursor.fetchall()
        for x in myd:
            print(myd)
            time.sleep(2)
            admin_menu()
        else:
            time.sleep(5)
            admin_menu()


def customer():
    print("Welcome to the Customer Menu ")
    print("Before getting started we require some information from you ")
    print("This information will not be shared, it simply expands the details on your account ")
    choice = input(" ")
    
start_menu()
