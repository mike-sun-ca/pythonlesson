#list lesson
#parentheses  tuple
#square brackets list
#curly brackets dict

from html.parser import HTMLParser
from html.entities import name2codepoint

a= ["a","b","c"]

print("the first item/value:",a[0])
print("the last item:",a[-1])
print("the totle items number:", len(a))

a.append("d")
print(a)
a.insert(0,"x")
print(a)
print("return a new list form index -3:", a[-3:])
a.pop(0)
print(a)
a.pop()
print(a)
a[1]="2"
print(a)
for myTxt in a:
    print("a have :", myTxt)
if "a" in a:
    print("a is an item in list a")
else:
    print("a not include in list a")

a += ["x","y","z"]
print(a)

print(a.count("a"))