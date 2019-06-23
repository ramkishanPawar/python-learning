"""@author: Ramkishan K Pawar
program to get the factorial of a number
using for loop"""

number = 6

product = 1

for num in range(2, number + 1):
    product *= num

print("The factorial of number {} is {}".format(number,product))
