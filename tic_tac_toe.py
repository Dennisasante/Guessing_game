def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

row2[1] = "X"

display(row1, row2, row3)

def user_choice():
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False


    while choice.isdigit() == False or within_range == False:

        choice = input("Enter a number(0-10): ")

        if choice.isdigit() == False:
            print("Sorry,this is not a digit!")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of the acceptable range(0-10)")
                within_range = False

    return int(choice)

user_choice()