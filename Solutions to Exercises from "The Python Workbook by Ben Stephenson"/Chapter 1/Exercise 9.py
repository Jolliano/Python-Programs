# This script calculates the compound interest.

deposit = ""
while deposit == "":
    a = input("Enter your initial deposit: ")
    if a.isdecimal():
        deposit = int(a)
    else:
        print("Please enter a valid deposit")
year1 = deposit * 1.04
year2 = year1 * 1.04
year3 = year2 * 1.04

print("The amount in the account after year 1 is " + "${:.2f}".format(year1))
print("The amount in the account after year 2 is " +"${:.2f}".format(year2))
print("The amount in the account after year 3 is " +"${:.2f}".format(year3))
