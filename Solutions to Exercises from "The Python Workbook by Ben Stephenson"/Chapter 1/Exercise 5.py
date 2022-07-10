#This program calculates the refunds given to customers based on the volume and numbere of bottles they return.

number_big = ""
number_small = ""
while number_big == "":
    a = input("Enter the number of big bottles i.e. bottles bigger than 1 liter: ")
    if a.isdecimal():
        number_big = int(a)
    else:
        print("Please enter a number")
while number_small == "":
    a = input("Enter the number of small bottles i.e. bottles smaller than 1 liter: ")
    if a.isdecimal():
        number_small = int(a)
    else:
        print("Please enter a number")
big_refund = number_big * 0.25
small_refund = number_small * 0.10

total_refund = big_refund + small_refund

total_2dp = "${:.2f}".format(total_refund)

print("Total refund for the number of bottles is " + total_2dp)
