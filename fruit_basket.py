"""@author: Ramkishan K Pawar
program to print the total no. of fruits and non-fruits
items availble in a fruit basket. Using a list fruits to
identify the fruits.
"""

no_of_fruits, not_fruits = 0,0

basket_items = {"Apples": 4, "Oranges": 19, "Kites": 3, "Sandwiches": 8,
                "Bananas": 2}

fruits = ["Apples", "Oranges", "Grapes", "Bananas", "Mangos", "Sapote"]

for key, value in basket_items.items():
    if key in fruits:
        no_of_fruits += value

#   else:
#       not_fruits += value

    elif key not in fruits:
        not_fruits += value

print("There are total {} fruits, {} non-fruit items in the basket".format(no_of_fruits,not_fruits))
