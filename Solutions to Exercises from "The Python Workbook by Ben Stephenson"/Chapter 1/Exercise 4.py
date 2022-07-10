#This program reads the length and width from the user and calculates the area of a field.

length = ""
width = ""
while length == "":
    a = input("Enter the length of the field in feet: ")
    if a.isdecimal():
        length = int(a)
    else:
        print("Please enter a number")
while width == "":
    b = input("Enter the width of the field in feet: ")
    if b.isdecimal():
        width = int(b)
    else:
        print("Please enter a number")
area = length * width / 43560

#Using the str.format() to control number of decimal places
area_2dp = "{:.2f}".format(area)

print("The area of the field is " + area_2dp + " acres")
