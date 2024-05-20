# # This is a sample Python script.
#
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
name = "Dennis"
age = 19
print(f'my name is {name} and I am {age} years old')
print(name, age)

myname="DennisAsante"
print("My name is "+myname[::])
print("My name is "+ myname)
print(myname.upper())
print(myname.split())
print("My name is {a} {d} {m} {f}".format(d="Dennis",m="McQwesi",f="Frimpong",a="Asante"))
print(len(myname))

set1 = [1, 2, 3, 4]
set2 = [5, 6, 7, 8]
set3 = [set1+set2]
set4 = [10, 11, 12, 12, 14, 15, 16, 17 ,18, 19, 20]
set2[0] = 90
print(set1 + set2)
print(set3)

print(1>10)
print(type(False))


if myname == "DennisAsante":
    print("Indeed, my name is DennisAsante")
else:
    print("Sorry, but my name is McQwesi")

fullname = ["Dennis", "McQwesi", "Frimpong", "Asante"]
for names in fullname:
    print(names)

print(set4)
for num in set4:
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number: {num}")

initialNumber = 0
for item in set4:
    initialNumber = initialNumber + item
print(initialNumber)

for _ in "DennisAsante":
    print("Hello")


for _ in [1,2,3,4]:
    #
    pass
print("end of script")

for num in range(10):
    print(num)

# result = input("What is your name? ")
# print(result + ",I see")
# if result == "Dennis":
#     print("So, Dennis is indeed your name")
# else:
#     print("This is not your name")

thislist = []
for _ in "Dennis":
    thislist.append(_)
print(thislist)

def new_function():
    print("hello")
    print("How are you doing today?")
    print("I hope all is well")

# new_function()

def dennis(name = "Asante"):
    print(f"Hello {name}")
dennis("Dennis")

def add_num(num1,num2):
    return num1+num2
result = add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

result = print_result(10,30)
print(type(result))
result = return_result(10,60)
print(result)
return_result(50,50)


print(20 % 2 == 0)

def even_check(num):
    return num % 2 == 0

print(even_check(21))


even_list = []
def check_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

print(check_list([1,2,3,4,5,6,7,8,9,10]))

work_hours = [("Dennis", 70),("McQwesi", 3000),("Asante", 900)]

def work_list(work_hours):

    current_hours = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_hours:
            current_hours = hours
            employee_of_month = employee
        else:
            pass

    return(current_hours,employee_of_month)

print(work_list(work_hours))

