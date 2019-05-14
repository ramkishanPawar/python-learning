"""
@author: Ramkishan K Pawar
Simple program to demonstrate functions in python
"""


def addition(a, b):

    addition = a + b
    return addition

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

getSum = addition(num1, num2)
print("The addition of " + str(num1) + " and " + str(num2) + " is " + str(getSum))
