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
    staffid = 1
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
        cursor.execute("SELECT MAX(Staff_ID) FROM Staff_Data")
        rawID = cursor.fetchone()
        ID = rawID[0] + 1
        userdata = [ID, username, password, level]
        sql = "insert into Staff_Data(Staff_ID, Username, Password, Level) values (?, ?, ?, ?)"
        cursor.execute(sql,userdata)
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
    choice = input("Would you like to view data?(Y/N) ")
    if choice == "Yes" or choice == "yes" or choice == "Y" or choice == "y":
        viewdata()
    elif choice == "No" or choice == "no" or choice == "N" or choice == "n":
        choice1 = input ("Would you like to edit data?(Y/N) ")
        if choice1 == "Yes" or choice1 == "yes" or choice1 == "Y" or choice1 == "y":
            editdata()
        elif choice1 == "No" or choice1 == "no" or choice1 == "n" or choice1 == "N":
        #    choice2 = input("Would you like to exit to the Customer menu? ")
            #if choice2 == "Yes" or choice2 == "yes" or choice2 == "Y" or choice2 == "y":
                #customer()
            #elif choice2 == "No" or choice2 == "no" or choice2 == "N" or choice == "n":
            admin_menu()

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
        viewdata()



#This will print the entirety of the Customer Data in the Customer Table.
def viewcustomer():
    print(" ")
    print("You have chosen to view Customer data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer")
        vc = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender","DOB"))
        for data in vc:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    admin_menu()

#Global inputname allows us to view the inputted usernames data
def md():
    print(" ")
    print("You have chosen to view your data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        md = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender","DOB"))
        for data in md:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

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
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20}".format("Ticket ID","Staff ID","Username","Vehicle Reg","Purchase Date","Duration","Fee Paid"))
        for data in td:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))


    admin_menu()
#This is the 'start menu' directing you around to the different edit options
def editdata():
    print(" ")
    print("You have chosen to edit data ")
    choice = input("Would you like to edit Customer data(C),Your Data(MD) or Exit(E)? ")
    if choice == "Customer" or choice == "customer" or choice == "C" or choice == "c":
        editcustomer()
    elif choice == "MD" or choice == "md":
        emd()
    #elif choice == "Ticket Data" or choice == "ticket data" or choice == "TD" or choice == "td":
    #    etd()
    elif choice == "Exit" or choice == "exit" or choice == "E" or choice == "e":
        sys.exit()
    else:
        editdata()

#User is global so that it can recognise who is being edited the through the entire procces
def editcustomer():
    global user
    print(" ")
    print("You have chose to edit customer data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer")
        ec = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender","DOB"))
        print(" ")
        for data in ec:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

        print(" ")
        user = input("Which user do you wish to edit? ")
        print("You have chosen to edit %s " %user)


        quser = input("Would you like to edit %s's Vehicle Registration(1), First Name(2), Last Name(3) or Gender(4)? " %user)
        if quser == "1":
            ecustlp()
        elif quser == "2":
            ecustfn()
        elif quser == "3":
            ecustln()
        elif quser == "4":
            ecustgen()
        else:
            editcustomer()

#def ecustuser():
#    print(" ")
#    print("You have decided to edit %s's Username " %user)
#    ncustuser = input("What would you like to change %s's Username to? " %user)
#    with sqlite3.connect("neapp.db") as db:
#        cursor = db.cursor()
#        cursor.execute("UPDATE Customer SET Username = '{0}' WHERE Username = '{1}'".format(ncustuser, user))
#        db.commit()
#        cursor.execute("SELECT * FROM Customer")
#        ecus = cursor.fetchall()
#        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
#        print(" ")
#        for data in ecus:
#            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
#
#
#    admin_menu()


def ecustlp():
    print(" ")
    print("You have decided to edit %s's License Plate " %user)
    ncustlp = input("What would you like to change %s's License Plate to? " %user)
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Vehicle_Reg = '{0}' WHERE Username = '{1}'".format(ncustlp, user))
        db.commit()
        cursor.execute("SELECT * FROM Customer")
        ecuslp = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecuslp:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

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
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB",))
        print(" ")
        for data in ecfn:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

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
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecln:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
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
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in ecgen:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    admin_menu()


def emd():
    print(" ")
    print("You have decided to edit your data ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute(" SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        md = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender","DOB"))
        for data in md:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    print(" ")
    choice = input("Would you like to edit your Vehicle Registration(1), First Name(2), Last Name(3) or Gender(4)? ")
    if choice == "1":
        emlp()
    elif choice == "2":
        emfn()
    elif choice == "3":
        emln()
    elif choice == "4":
        emgen()
    else:
        admin_menu()

#def emuser():
#    print(" ")
#    print("You have decided to edit your username ")
#    emuser = input("What would you like to change your Username to? ")
#    with sqlite3.connect("neapp.db") as db:
#        cursor = db.cursor()
#        cursor.execute(" UPDATE Customer SET Username = '{0}'WHERE Username = '{1}'".format(emuser, inputname))
#        db.commit()
#        cursor.execute("SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
#        db.commit()
#        emuser = cursor.fetchall()
#        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender","DOB"))
#        for data in emuser:
#            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

#    admin_menu()
    

def emlp():
    print(" ")
    print("You have decided to edit your License Plate ")
    nmlp = input("What would you like to change your License Plate to? ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Vehicle_Reg = '{0}' WHERE Username = '{1}'".format(nmlp, inputname))
        db.commit()
        cursor.execute("SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        emlp = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in emlp:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))

    admin_menu()

def emfn():
    print(" ")
    ("You have decided to edit your First Name ")
    nmfn = input("What would you like to change your First Name to? ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET First_Name = '{0}' WHERE Username = '{1}'".format(nmfn, inputname))
        db.commit()
        cursor.execute("SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        emfn = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in emfn:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    admin_menu()

def emln():
    print(" ")
    print("You have decided to edit your Last Name ")
    nmln = input("What would you like to change your Last Name to? ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Last_Name = '{0}' WHERE Username = '{1}'".format(nmln, inputname))
        db.commit()
        cursor.execute("SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        emln = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in emln:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    admin_menu()

def emgen():
    print(" ")
    print("You have decided to edit your Gender ")
    nmgen = input("What would you like to change your Gender to? ")
    with sqlite3.connect("neapp.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Customer SET Gender = '{0}' WHERE Username = '{1}'".format(nmgen, inputname))
        db.commit()
        cursor.execute("SELECT * FROM Customer WHERE Username = '{0}'".format(inputname))
        emgen = cursor.fetchall()
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Username","Vehicle Reg","First Name","Last Name","Gender", "DOB"))
        print(" ")
        for data in emgen:
            print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
    admin_menu()
#def etd():
#    print(" ")
#    print("You have decided to edit ticket data ")
#    with sqlite3.connect("neapp.db") as db:
#        cursor = db.cursor()
#        cursor.execute(" SELECT * FROM Tickets")
#        etd = cursor.fetchall()
#        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20}".format("Ticket_ID","Staff_ID","Username","Vehicle_Reg","Purchase_Date","Duration","Fee_Paid"))
#        for data in etd:
#              print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
#              
#        print(" ")
#        Ticket = input("Which ticket do you wish to edit?(Please select a Ticket_ID) ")
#        print("You have chosen to edit Ticket %s " %Ticket)
#        qticket = input("Would you like to edit Tickets %s's Username(1), Vehicle Registration(2), Purchase Date(3) or Fee Paid(4)? "%Ticket)
#        if qticket == "1":
#            eticuser()
#        elif qticket == "2":
#            etickreg()
#        elif qticket == "3":
#            etickdate()
#        elif qticket == "4":
#            etickfee()
#        else:
#            admin_menu()          

#    admin_menu()   







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
