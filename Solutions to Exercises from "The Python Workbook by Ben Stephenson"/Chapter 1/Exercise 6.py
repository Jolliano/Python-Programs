#This program calculates the tax and tip for meals.

cost = ""
tax_percent = 0.1
tip_percent = 0.18

while cost == "":
    a = input("Please enter the cost of the meal")
    if a.isdecimal():
        cost = int(a)
    else:
        print("Please enter a number")

tax_amount = cost * tax_percent
tip_amount = cost * tip_percent
total = cost + tax_amount + tip_amount

tax_amount = "${:.2f}".format(tax_amount)
tip_amount = "${:.2f}".format(tip_amount)

print("The tax amount is " + tax_amount)
print("The tip amount is " + tip_amount)
print("The total cost is " + "{:.2f}".format(total))
