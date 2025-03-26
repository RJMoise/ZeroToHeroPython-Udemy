# Cup Guess
#guess which cup the ball is under

#Import
from random import shuffle

#Inital list
mylist = [' ', 'O', '']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2! ")
    
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(mylist)

# Shuffle List
mixedup_list = shuffle_list(mylist)

# Player Guess
guess = player_guess()

#Check Results
check_guess(mixedup_list, guess)