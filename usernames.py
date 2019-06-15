"""@author: Ramkishan K Pawar
program to convert a given nameslist into usernames"""

names = ["Ramkishan Pawar", "Madhuri Jaju", "Sonal Patwari", "Yashika Lalwani", "Arjun Londhe", "Payal Roul"]

usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

