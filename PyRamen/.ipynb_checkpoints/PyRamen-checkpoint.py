"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path


#set the output of the text file
text_path = "output.txt"


# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath= Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Initialize line_num variable
line_num = 0

# @TODO: Read in the menu data into the menu list

# Open the input path as a file object 
with open(menu_filepath, 'r') as menufile:

    # Print the datatype of the file object
        #print(type(menufile))

  # Pass in the menu file to the menu.reader() function
    # (with ',' as the delmiter/separator) and return the menureader object
        menureader = csv.reader(menufile, delimiter=',')
    
    # Print the datatype of the menureader
    #print(type(menureader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
        header = next(menureader)
        line_num += 1
    # Print the header
    #print(f"{header} <---- HEADER")

    # Read each row of data after the header
    
        for row in menureader:
            # Print the row
            #print(row)
            # Append menu list 
            menu=list(menureader)
        
        #print(menu)

# @TODO: Read in the sales data into the sales list

line_num=0    
# Open the input path as a file object 
with open(sales_filepath, 'r') as salesfile:

    # Print the datatype of the file object
    #print(type(salesfile))

  # Pass in the menu file to the menu.reader() function
    # (with ',' as the delmiter/separator) and return the menureader object
    salesreader = csv.reader(salesfile, delimiter=',')
    
    # Print the datatype of the salesreader
    #print(type(salesreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    #header = next(salesreader)
    line_num += 1
    # Print the header
    #print(f"{header} <---- HEADER"
    
    for row in salesreader:
    #Print the row
    #print(row)
        sales=list(salesreader)
 
    #print(sales)
    
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for row_count in range(len(sales)):
    row_count+=1

# Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item

# @TODO: Initialize sales data variables
Line_Item_ID=0
Date='DD-MON-YYYY'
Credit_Card_Number=0
Quantity=0
Menu_Item=''

# @TODO:
# If the item value not in the report, add it as a new entry with initialized metrics
# Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

count=0
revenu=0
cost=0
profit=0


for row_sales in range(len(sales)):
    for row_menu in range(len(menu)):
        if menu[row_menu][0] == sales[row_sales][4]:
            count += 1     
            revenu = revenu + int(sales[row_sales][3])*int(menu[row_menu][3])
            cost= cost + int(sales[row_sales][3])*int(menu[row_menu][4])
    
    profit=revenu/cost
    report=[(menu[row_menu][0]), count,revenu, cost,profit]
    print(report)
                
    
# @TODO: For every row in our sales data, loop over the menu records to determine a match

  
# Item,Category,Description,Price,Cost

# @TODO: Initialize menu data variables
item=''
category=''
description=''
price=0
cost=0 
Match= {}

for i in range(len(sales)):
    for x in range(len(menu)):
        if item == menu[x][0]:
            Item=menu[x][0]
            Category=menu[x][1]
            Description=menu[x][2]
            Price=int(menu[x][3])
            Cost=int(menu[x][4])
            
            match=[Item,Category,Description,Price,Cost]
        
            print(match)
        

# @TODO: Calculate profit of each item in the menu data

#for row_sales in range(len(sales)):
for row_menu in range(len(menu)):
    if menu[row_menu][0] == sales[row_sales][4]:
              revenu = revenu + int(sales[row_sales][3])*int(menu[row_menu][3])
              cost= cost + int(sales[row_sales][3])*int(menu[row_menu][4])
            
              profit=revenu/cost
                  
    print(menu[row_menu][0], profit)
    
# @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


# @TODO: Print out matching menu data

#for row_sales in range(len(sales)):
for row_menu in range(len(menu)):
    if menu[row_menu][0] == sales[row_sales][4]:
        print(menu[row_menu])

# @TODO: Cumulatively add up the metrics for each item key

count=0
for i in range(len(sales)):
    for row_menu in range(len(menu)):
        if menu[row_menu][0] == sales[i][4]:
            # @TODO: Increment the row counter by 1
            count+=1
            
# @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match

        elif menu[row_menu][0] != sales[row_sales][4]: 
            pass


# @TODO: Print total number of records in sales data
        total_record=len(sales)

# @TODO: Write out report to a text file (won't appear on the command line output)
  #write changes to csv
with open(text_path, 'w') as file:
    file.write(" PyRamen Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Sales list Objects: %d\n" % row_count)
    file.write("Report: %s\n" % str(report) )
    
    
        


