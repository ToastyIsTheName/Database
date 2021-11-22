#Cornershop program

import sqlite3, sys, time, os

from banner import *

cmd = 'mode 80,30'
os.system(cmd)
os.system("color B1")

def menu():
    os.system('cls')
    banner()
    print(" ")
    choice = input("Press 1 to view stock,2 to add new stock, 3 to add a sale or 4 to exit  ")
    if choice == "1":
        view_stock()
    elif choice == "2":
        add_stock()
    elif choice == "3":
        add_sale()
    elif choice == "4":
        sys.exit()
    else:
        print("Please enter a valid choice...")
        time.sleep(1)
        menu()

def view_stock():
    os.system('cls')
    banner()
    print(" ")
    db = sqlite3.connect("cornershop.db")
    cursor = db.cursor ()
    sql = "select * from stock"
    cursor.execute(sql)
    all_stock = cursor.fetchall()

    print(" ")
    print (" {0:<10} {1:<20} {2:<10} {3:<10} {4:<10}".format("StockID","Description","Price","Quantity","Sell by"))
    for stock in all_stock:
        print(" {0:<10} {1:<20} {2:<10} {3:<10} {4:<10}".format(stock[0],stock[1],stock[2],stock[3],stock[4]))
    pressany = input("Press any key to continue")
    menu()

def view_stock2():
    os.system('cls')
    banner()
    print(" ")
    db = sqlite3.connect("cornershop.db")
    cursor = db.cursor ()
    sql = "select * from stock"
    cursor.execute(sql)
    all_stock = cursor.fetchall()

    print(" ")
    print (" {0:<10} {1:<20} {2:<10} {3:<10} {4:<10}".format("StockID","Description","Price","Quantity","Sell by"))
    print (" ")
    for stock in all_stock:
        print(" {0:<10} {1:<20} {2:<10} {3:<10} {4:<10}".format(stock[0],stock[1],stock[2],stock[3],stock[4]))
    print(" ")
    pressany = input("Press any key to continue")

def add_stock():
    os.system('cls')
    banner()
    print(" ")
    description = input("Enter a description of the item ")
    price = input("Enter the price ")
    quantity = input("Enter the quantity ")
    sell_by_date = input("Enter the sell by date ")
    data = (description,price,quantity,sell_by_date)
    db = sqlite3.connect("cornershop.db")
    cursor = db.cursor()
    sql = "INSERT INTO stock(description,price,quantity,sell_by_date) VALUES (?,?,?,?)"
    cursor.execute(sql,data)
    db.commit()
    pressany = input("Press any key to continue")
    menu()

def add_sale():
    os.system('cls')
    banner()
    print(" ")
    print("This is the current stock in the shop")
    view_stock2()
    print(" ")
    customer = input("Enter the customer's name ")
    staff = input("Enter the staff name ")
    sale_date = input("Enter the date of the sale ")
    while True:
        print("Enter the details for each product")
        stockID = input("Enter the stock ID ")
        price = float(input("Enter the price "))
        quantity = int(input("Enter the quantity "))
        total = price*quantity
        data = (stockID,price,quantity,total,customer,staff,sale_date)
        db = sqlite3.connect("cornershop.db")
        cursor = db.cursor()
        sql1 = "INSERT INTO sales(stockID,price,quantity,total,customer,staff,sale_date) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(sql1,data)
        db.commit()
        sql2 = "SELECT quantity FROM stock WHERE stockID = %s" %stockID
        cursor.execute(sql2)
        oldquantity = str(cursor.fetchone())
        oldquantity = oldquantity.strip("(,) ")
        oldquantity = int(oldquantity)
        newquanitity = oldquantity - quantity
        sql3 = "UPDATE stock SET quantity = '%s' WHERE stockID = '%s'" % (newquanitity,stockID)
        cursor.execute(sql3)
        db.commit()
        choice = input("Do you wish to purchase another item? ")
        if choice == "Y":
            shopagain = input("Press any key to continue shopping ")
        else:
            break
    pressany = input("Press any key to continue")
    menu() 

menu()
