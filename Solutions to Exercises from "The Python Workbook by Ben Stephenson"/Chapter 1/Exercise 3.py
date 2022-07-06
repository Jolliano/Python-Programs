# This script calculates the area of a room using the measurements input by the user.

print("Welcome to the Room Area Calculator.")
w = 0
l = 0

while w == 0:
    w_ans = input("Enter the width of the room. This value should be in meters.  ")
    if w_ans.isdecimal():
        w = float(w_ans)
    else:
        print("Please enter a number only")

while l == 0:
    l_ans = input("Enter the length of the room. This value should be in meters.  ")
    if l_ans.isdecimal():
        l = float(l_ans)
    else:
        print("Please enter a number")

area = w * l

print("The area of the room is " + str(area) + " square meters.")
