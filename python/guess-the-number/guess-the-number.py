import random

def guess (high_numbr):
    random_number= random.randint(1,high_numbr)
    is_correct= False

    while is_correct==False:
        guess = int(input(f'insert your guess number between 1 - {high_numbr}:'))
        is_correct = check_number(guess,random_number)       
    print (f'congrats,you have geassed the number {random_number} correctly')

def check_number (guess,corect_number):
    if guess == corect_number:
        return True
    if guess < corect_number:
        print ('too low , guess again')
        return False
    if guess > corect_number:
        print ('too high, guess again')
        return False



higher_numbr= int ( input ('insert number '))
guess (higher_numbr)
