def myfunc(name):
    print("Hello " + name)

myfunc("Dennis")

def summit(a,b,c,d,e):
    return sum((a,b,c,d,e)) * 0.15

print(summit(40,60,100,100,3))

def newfunc(a, b):
    return sum((a, b)) * 0.05

print(newfunc(40,60))

import random

print(random.randrange(1, 10))

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

mylist = ["apple","banana","melon","orange","cherry","grape","coconut"]
#
newlist = [x for x in mylist if "a" in x]

print(newlist)

a = 2
b = 330
print("A") if a > b else print("B")

def my_function():
    print("Hello from a function")

my_function()


names = ["Dennis","Frimpong","Asante"]
name = len(names)

print(name)

username = input("Enter username: ")
print("Your user name is "+ username+"17")