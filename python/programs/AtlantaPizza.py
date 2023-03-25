# AtlantaPizza.py
number_of_pizzas = eval(input("How many pizzas do you want?"))
cost_per_pizzas = eval(input("How much does each pizza cost?"))
subtotal = number_of_pizzas  *  cost_per_pizzas
tax_rate = eval(input("What is your tax rate?"))
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
print("The total cost is $" , total)
