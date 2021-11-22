#Ollie W-B
#Prototype Program

#imports time so I can add natural pauses between outputs. Makes it seem more human
import time
#Connects Python to SQL so the database can work
import sqlite3
import random
import sys
#Imports the banner file I created so the companys software is 'watermarked'
from Banner1 import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         TO DO                                ||
#                                                              ||
#Add more time/pauses and gaps. Make program seem more human   ||
#Ticket Menu - Calculating funds ETC                           ||
#Remove Customers - Admin System                               ||
#Make a way for edit access level - appointing admin           ||                                                                           
#Make a way for tickets to be added                            ||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         UPDATED                              || ### ADD ALL HERE TO UPDATED PROTOTYPE###
#Customers can now input personal data upon registering        ||
#Formatting issues have been sorted                            ||
#Turned into an administrative system                          ||
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


#The Register menu will include more questions to gain extra data but I didn't think the prototype needed the extra detail yet.        
def register():
#This generates a random 2 digit number
    number = random.randint(10,99)
    level = "Administrator"
    staffid = " "
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
        userdata = [staffid, username, password, level]
        sql = "insert into Staff_Data(Staff_ID, Username, Password, Level) values (?, ?, ?, ?)"
        cursor.execute(sql,userdata)
        db.commit()
    username = input("Your username is %s" %username)
    fname = input("Please enter your First Name: ")
    vlp = input("Please enter your Vehicle's Registration: ")
    lname = input("Please enter your Last Name: ")
    gen = input("Please enter your Gender: ")
    dob = input("Please enter your Date Of Birth: ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        customerinf = [username, fname, lname, gen, dob] 
        sql = "insert into Customer(Username, Vehicle_Reg, First_Name, Last_Name, Gender, DOB) values (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, customerinf)
        db.commit()
        print("Your data has been added to our system ")
        print(" ")
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
        cursor.execute(" SELECT Username FROM Staff_Data WHERE Username = '%s'" %inputname)
        name = str(cursor.fetchone())
        username = name.strip(" (),' ")

    if inputname ==username:
        print("Your username has been recognised ")
        inputpwd = input("Please input your password ")
#This is selecting the passwords from the saved accounts to see if the inputted password matches any
        cursor.execute(" SELECT password FROM Staff_Data WHERE Username = '%s'" %inputname)
        password = str(cursor.fetchone())
        password = password.strip(" (),' ")


        if inputpwd == password:
            print("Your password has been recognised ")
            cursor.execute(" SELECT level FROM Staff_Data WHERE Username = '%s'" %inputname)
            level = str(cursor.fetchone())
            level = level.strip(" (),' ")
            print("Your access level is %s" %level)
#This checks if you hold the User or Administrator role so it can decide what you can view.
            if level == "Administrator":
                admin_menu()
            #else:
            #    print("You do not have access to the administrator menu ")
            #    customer()
        else:
            print("The password you have entered doesn't match the given username. Please try again ")
            login()
    else:
        print("The username you have inputted has not been recognised. Please try again ")
        login()
            
            

#The administrator menu helps you navigate to all the administrator perks
#choice = View Data
#choice1 = Edit Data
#choice2 = Exit to Customer Menu
def admin_menu():
    print(" ")
    time.sleep(0.5)
    print("Welcome to the Administrator Menu ")
    time.sleep(1)
    choice = input("Would you like to view data? ")
    if choice == "Yes" or choice == "yes" or choice == "Y" or choice == "y":
        viewdata()
    elif choice == "No" or choice == "no" or choice == "N" or choice == "n":
        choice1 = input ("Would you like to edit data? ")
        if choice1 == "Yes" or choice1 == "yes" or choice1 == "Y" or choice1 == "y":
            editcustomer()
        elif choice1 == "No" or choice1 == "no" or choice1 == "n" or choice1 == "N":
        #    choice2 = input("Would you like to exit to the Customer menu? ")
            #if choice2 == "Yes" or choice2 == "yes" or choice2 == "Y" or choice2 == "y":
                #customer()
            #elif choice2 == "No" or choice2 == "no" or choice2 == "N" or choice == "n":
            sys.exit()

    else:
        admin_menu()


#Here you choose what data you would like to view
def viewdata():
    print(" ")
    print("You have chosen to view data")
    choice = input("Would you like to view Customer Data(C), Your Data(MD), Ticket Data(TD) or Exit(E)? ")
    if choice == "Customer" or choice == "customer" or choice == "C" or choice == "c":
        viewcustomer()
    elif choice == "MD" or choice == "md":
        md()
    elif choice == "Ticket" or choice == "TD" or choice == "td":
        viewtd()
    elif choice == "Exit" or choice == "exit" or choice == "E" or choice == "e":
        sys.exit()
    else:
        admin_menu()



#This will print the entirety of the Customer Data in the Customer Table.
def viewcustomer():
    print(" ")
    print("You have chosen to view Customer data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer")
        vc = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Username","First Name","Last Name","Gender","DOB"))
        for data in vc:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(data[0],data[1],data[2],data[3],data[4]))
    admin_menu()

#Global inputname allows us to view the inputted usernames data
def md():
    print(" ")
    print("You have chosen to view your data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        md = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Username","First Name","Last Name","Gender","DOB"))
        for data in md:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(data[0],data[1],data[2],data[3],data[4]))

    admin_menu()
#This prints ALL Ticket Data
def viewtd():
    print(" ")
    print("You have chosen to view Ticket Data ")
    print(" ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Tickets ")
        td = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Ticket ID","Purchase Date","Duration","Valid Until","Fee Paid"))
        for data in td:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(data[0],data[1],data[2],data[3],data[4]))


    admin_menu()
#This is the 'start menu' directing you around to the different edit options
def editdata():
    print(" ")
    print("You have chosen to edit data ")
    choice = input("Would you like to edit Customer data(C),Your Data(MD), Ticket Data(TD) or Exit(E)? ")
    if choice == "Customer" or choice == "customer" or choice == "C" or choice == "c":
        editcustomer()
    elif choice == "MD" or choice == "md":
        emd()
    elif choice == "Ticket Data" or choice == "ticket data" or choice == "TD" or choice == "td":
        emd()
    elif choice == "Exit" or choice == "exit" or choice == "E" or choice == "e2":
        sys.exit()
    else:
        start_menu()

#User is global so that it can recognise who is being edited the through the entire procces
def editcustomer():
    global user
    print(" ")
    print("You have chose to edit customer data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer")
        ec = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20}".format("Username","First Name","Last Name","Gender","DOB"))
        print(" ")
        for data in ec:
            print("{0:<20} {1:<20} {2:<20} {3:<20}".format(data[0],data[1],data[2],data[3]))

        print(" ")
        user = input("Which user do you wish to edit? ")
        print("You have chosen to edit %s " %user)


        quser = input("Would you like to edit %s's Username(1), First Name(2), Last Name(3) or Gender(4)? " %user)
        if quser == "1":
            ecustuser()
        elif quser == "2":
            ecustfn()
        elif quser == "3":
            ecustln()
        elif quser == "4":
            ecustgen()
        else:
            admin_menu()

def ecustuser():
    print(" ")
    print("You have decided to edit %s's Username " %user)
    ncustuser = input("What would you like to change %s's Username to? " %user)
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Username = '{0}' WHERE Username = '{1}'".format(ncustuser, user))
        db.commit()
        cursor.execute("SELECT * FROM Customer")
        ecus = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20}".format("Username","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecus:
            print("{0:<20} {1:<20} {2:<20} {3:<20}".format(data[0],data[1],data[2],data[3]))


    admin_menu()

def ecustfn():
    print(" ")
    print("You have decided to edit %s's First Name " %user)
    ncustfn = input("What would you like to change %s's First Name to? " %user)
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET First_Name = '{0}' WHERE Username = '{1}'".format(ncustfn, user))
        db.commit()
        cursor.execute("SELECT * FROM Customer")
        ecfn = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20}".format("Username","First Name","Last Name","Gender", "DOB",))
        print(" ")
        for data in ecfn:
            print("{0:<20} {1:<20} {2:<20} {3:<20}".format(data[0],data[1],data[2],data[3]))

    admin_menu()


def ecustln():
    print(" ")
    print("You have decided to edit %s's Last Name " %user)
    ncustln = input("What would you like to change %s's Last Name to? " %user)
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Last_Name = '{0}' WHERE Username = '{1}'".format(ncustln, user))
        db.commit()
        cursor.execute("SELECT * FROM Customer")
        ecln = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20}".format("Username","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecln:
            print("{0:<20} {1:<20} {2:<20} {3:<20}".format(data[0],data[1],data[2],data[3]))
    admin_menu()

def ecustgen():
    print(" ")
    print("You have decided to edit %s's Gender " %user)
    ncustgen = input("What would you like to change %s's Gender to? " %user)
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Gender = '{0}' WHERE Username = '{1}'".format(ncustgen, user))
        db.commit()
        cursor.execute("SELECT * FROM Customer")
        ecgen = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20}".format("Username","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecgen:
            print("{0:<20} {1:<20} {2:<20} {3:<20}".format(data[0],data[1],data[2],data[3]))
    admin_menu()


def emd():
    print(" ")
    print("You have decided to edit your data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        md = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Username","First Name","Last Name","Gender","DOB"))
        for data in md:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(data[0],data[1],data[2],data[3],data[4]))
    print(" ")
    choice = input("Would you like to edit your Username(1), First Name(2), Last Name(3) or Gender(4)? ")
    if choice == "1":
        emuser()
    elif choice == "2":
        emfn()
    elif choice == "3":
        emln()
    elif choice == "4":
        emgen()
    else:
        admin_menu()

def emuser():
    print(" ")
    print("You have decided to edit your username ")
    emuser = input("What would you like to change your Username to? ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" UPDATE Customer SET Username = '{0}'WHERE Username = '{1}'".format(emuser, inputname))
        emuser = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Username","First Name","Last Name","Gender","DOB"))
        for data in emuser:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(data[0],data[1],data[2],data[3],data[4]))
    

#def customer():
#    print(" ")
#    print("Welcome to the Customer Menu ")
#    choice = input("Would you like to View or Edit your data? ")
#    if choice == "View" or choice == "view" or choice == "V" or choice == "v":
#        md()
#    elif choice == "Edit" or choice == "edit" or choice == "E" or choice == "e":
#        emd()
#    else:
#        customer()



    
start_menu()
