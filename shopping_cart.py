
import pandas as pd 
import datetime

product_table = pd.read_csv("data/products.csv")
    # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

products = product_table.to_dict(orient='records')

product_ids = [item['id'] for item in products]

now = datetime.datetime.now()

receipt = []
subtotal = 0

#function below is to print of an item
def add_item(prod_ident):
    global subtotal
    if prod_ident in product_ids: 
        for prod in products:
            if prod_ident == prod["id"]: 
                var = print("Product: " + str(prod["name"]) + "        Price: " + str(to_usd(prod["price"])))
                receipt.append(prod)
                subtotal += prod["price"]
    else:
        var = "Hey, are you sure that product identifier is correct? Please try again!"
    return var
#function below is to convert a float to a USD string
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



prompt = "Please input product identifier, one product at a time: "
print("If done adding items, please enter DONE.")
identify_txt = ""
#code below is for error handling when the user is promoted to select 'Done'
while identify_txt != "DONE" or identify_txt != "Done" or identify_txt != "done":
    identify_txt = input(prompt)
    try:
        if identify_txt == "DONE" or identify_txt == "Done" or identify_txt == "done":
            print("Done adding items, Thank you")
            break
        else:
            identify_txt = int(identify_txt)
            add_item(identify_txt)
            if identify_txt not in product_ids:
                print("Product ID does not exist. Please enter a valid product identifier, or enter DONE to end.")
    except ValueError:
        print("Please enter a valid product identifier number, or enter DONE to end.")

tax = round(subtotal*.0875, 2)
total_amount = round(tax + subtotal, 2)
print("                            ")
print("See Purchase Summary Below:")
print("----------------------------")
print("Murray Hill Food Market \nwww.MHFM.com")
print("----------------------------")
print("CHECKOUT AT: " + str(now.strftime("%m/%d/%Y, %I:%M %p")))
print("----------------------------")
print("SELECTED PRODUCTS: ")
for item in receipt:
    print("..." + str(item["name"]) + " (" + str(to_usd(item["price"])) + ")")
print("----------------------------")
print("SUBTOTAL: " + str(to_usd(subtotal)))
print("TAX: " + str(to_usd(tax)))
print("TOTAL: " + str(to_usd(total_amount)))
print("----------------------------")
print("THANK YOU, SEE YOU AGAIN SOON!")
print("----------------------------")


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

#Step4: Build the application to store product info in a CSV