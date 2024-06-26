from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

mylist = ["0", " ", " "]
shuffle_list(mylist)

def player_guess():
    guess = " "
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0,1, or 2 : ")
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == "0":
        print("correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# INITIAL LIST
mylist = ["0", " ", " "]

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list, guess)