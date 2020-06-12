# Shopping_Cart_Project
The following is a README file for the instructions on how to use the shopping cart program

Setup: The user should run "shopping_cart.py" to run the program

Steps:

1. The user is prompted to input a product identifier, and when done to type "Done".
    * Error Handling: If the user types a product identifier that does not exist, he/she will get an error notifying the user.
        * Error Message - "Product ID does not exist. Please enter a valid product identifier, or enter DONE to end."
    * Error Handling: If the user enters letters as product identifiers and not numbers, he/she will receive the following message:
        * Error Message - "Please enter a valid product identifier, or enter DONE to end."

2. Once the user types a number (ex.1), the program will display the product name and the price
* The program will continue to ask the user to add products until the user types "Done". 
* All product data is stored and retrieved from a CSV file within the 'data' sub repository.

3. As the user continues to add items, those items are added to a receipt.

4. Once the user types "Done", he/she is presented with a purchase summary that includes the following:
    * Checkout Date & Time
    * List of Selected Products
    * Purchase Subtotal
    * Purchase Tax
    * Purchase Total
    * Thank you message to the user