# Shopping_Cart_Project


#raise errors if needed using conditional statements
#raise Mycustomerror("My custom message")

#import datetime module if needed

#objective: Modernize the checkout system
#considerations - each item has a price tag
#the cashier adds product prices for items purchased, with tax and a total amount
#can we have a system that will automatically look up prices using a barcode?
#Can we perform the calculations automatically and send a receipt? (using a GUI)
#Can we manage the code in a CSV or a Google spreadsheet?
#can we have a prompt to enter the customer email address to send a receipt?


#Step 1: Ask the clerk to input one or more product identifiers, one at a time
    #substep - Ensure the prodict identifier is correct, if not notify the clerk with the below message
        #"Hey are you sure that product identifier is correct? Please try again!"
    #substep - allow the clerk the abiloity to use the word "DONE" to indicate no more items are needed
        #Clear instructions for using DONE should be given asking for product identifiers

#Step2: Look up the price of each identifier

#Step3: Print an itemized customer receipt including total, tax, and grand total
    #substep - after the clerks indicates no more items, print a custom receipt on the screen with the following:
        #A grocery store name of your choice
        #A grocery store phone number and/or website URL and/or address of choice
        #The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
        #The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
        #The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
        #The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
        #The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
        #A friendly message thanking the customer and/or encouraging the customer to shop again

#Step4: Build the application to store inventory, products, prices in Google Sheets