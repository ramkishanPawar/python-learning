"""@author: Ramkishan K Pawar
program to iterate key value pair from a 
dictionary """

movies_cast = { "Coolie no 1": "Govinda",
                "Aunty NO 1" : "Govinda",
                "Phool Aur Kante": "Ajay Devgan",
                "Jhapatlela" : "Mahesh Kothare, Laximikant Berde",
                "Endgame" : "Robert Downey Jr."}

# This method will only print the keys
#
# for eachcast in movies_cast:
#    print(eachcast)

# Method to print the keys as well as values

for key, value in movies_cast.items():
    print("Movie: {} and the Cast is: {}".format(key,value))
