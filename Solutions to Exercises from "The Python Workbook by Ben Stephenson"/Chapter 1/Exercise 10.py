# This script carries out arithmetic on two inputs

a = 0
b = 0

from math import log10

while a == 0:
    first_num = input("Enter the first number: ")
    if first_num.isdecimal():
        a = int(first_num)
    else:
        print("Guy, na number you suppose type")
while b == 0:
    first_num = input("Enter the second number: ")
    if first_num.isdecimal():
        b = int(first_num)
    else:
        print("Guy, na number you suppose type")

print("The sum of the numbers is " + str(a+b))
print("The difference between a and b is " + str(a-b))
print("The product of a and b is " + str(a*b))
print("The quotient of a and b is " + str(int(a/b)))
print("The modulus of a and b is " + str(a%b))
print("The logarithm of a is " + str(log10(a)))
print("The value of a raised to power b is " + str(a**b))
