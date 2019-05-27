""" @author: Ramkishan K Pawar
Python Program to find a given number is even or
odd.
"""

number =int(input("Enter a number to find out if it's a even or odd: "))

if number % 2 == 0:
    print("The number {} is even !".format(number))
else:
    print("The number {} is odd !".format(number))
