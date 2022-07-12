# This script calculates the total weight.

weight_of_widget = 75
weight_of_gizmo = 112

widget_number = ""
gizmo_number = ""

while widget_number == "":
    a = input("Enter the number of widgets: ")
    if a.isdecimal():
        widget_number = int(a)
    else:
        print("Invalid entry")

while gizmo_number == "":
    a = input("Enter the number of gizmos: ")
    if a.isdecimal():
        gizmo_number = int(a)
    else:
        print("Invalid entry")

print("The total weight of your entry is " + str((widget_number*weight_of_widget)+(gizmo_number*weight_of_gizmo)) + " grams")
