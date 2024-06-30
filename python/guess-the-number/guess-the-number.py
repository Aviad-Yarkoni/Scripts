import random

def guess (high_numbr):
    random_number= random.randint(1,high_numbr)
    result = 1
    while result !=0:
        guess = int(input(f'insert your guess number between 1 - {high_numbr}:'))
        result = check_number(guess,random_number)
        if result ==1:
            print ('too low , guess again')
            guess = int(input(f'insert your guess number between 1 - {high_numbr}:'))
            result = check_number(guess,random_number)
        if result ==2:
            print ('too high, guess again')
            guess = int(input(f'insert your guess number between 1 - {high_numbr}:'))
            result = check_number(guess,random_number)

    print (f'congrats,you have geassed the number {random_number} correctly')

def check_number (guess,corect_number):
    if guess == corect_number:
        return 0
    if guess < corect_number:
        return 1
    if guess > corect_number:
        return 2



higher_numbr= int ( input ('insert number '))
guess (higher_numbr)
