"""@author: Ramkishan K Pawar
program to change the username list without using another list
with the help of range."""

usernames = ["Ramkishan Pawar", "Sonal Patwari", "Madhuri Jaju", "Yashika Lalwani", "Arjun Londhe"]

for eachusername in range(len(usernames)):
    usernames[eachusername] = usernames[eachusername].lower().replace(" ", "_")
    
print(usernames)
