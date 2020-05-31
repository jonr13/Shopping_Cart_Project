def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

products = []
receipt = []
dict = []

def add_item(prod_ident):
    if prod_ident in dict: 
        for prod in products:
            if prod_ident == prod["id"]:  
                var = print("Product: " + str(prod["name"]) + "        Price: " + str(to_usd(prod["price"])))
                receipt.append(prod)
    else:
        var = "Hey, are you sure that product identifier is correct? Please try again!"
    return var








    

