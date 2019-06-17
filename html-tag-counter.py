"""@author: Ramkishan K Pawar
program to count how many html elements are there
in a list """

tag_list = ["<html>", "<title>", "Hello World !", "</title>", "</html>"]

count = 0

for each_tag in tag_list:
    if each_tag[0] == '<' and each_tag[-1] == '>':
        count += 1

print("The total html tags are {} !".format(count))
