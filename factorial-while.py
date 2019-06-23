"""@author: Ramkishan K Pawar
program to find the factorial of a number
using while loop"""

number = 6

product = 1

current = 1

while current <= number:
    product *= current
    current += 1

print("The factorial of number {} is, {}.".format(number,product))
