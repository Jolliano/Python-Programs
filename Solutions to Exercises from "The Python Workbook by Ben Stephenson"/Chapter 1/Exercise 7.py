#This script calculates the sum of the first n positive integers

number = ""
total = 0
while number == "":
    a = input("Enter a number:  ")
    if a.isdecimal():
        number = int(a)
    else:
        print("Please enter a number")

for i in range(1,number+1):
    total = total + i

print ("The sum of the integers from 1 to " + str(number) + " is " + " is " + str(total))
