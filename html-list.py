"""@author: Ramkishan K Pawar
program to create html list using python."""

items = ["first string", "second string"]
html_str = "<ul>\n"

for each_item in items:
    html_str += "<li>{}</li>\n".format(each_item)
html_str += "</ul>"

print(html_str)
