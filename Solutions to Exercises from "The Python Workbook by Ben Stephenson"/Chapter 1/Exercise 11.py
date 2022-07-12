#This script converts the fuel efficiency from MPG to L/100 km

am_fe = ""

while am_fe =="":
    a = input("Enter the fuel efficiency in MPG: ")
    if a.isdecimal():
        am_fe = int(a)
    else:
        print("Please enter a number")

ca_fe = am_fe * 235.215

print("The fuel efficiency in Canadian units is " + str(int(ca_fe)) + " L/100 km")
