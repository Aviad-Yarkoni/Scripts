import random

def guess (high_numbr):
    random_number= random.randint(1,high_numbr)
    result = 1
    while result !=0:
        guess = input ('insert your guss number between 1 - ', random_number)
        result = check_number(guess,random_number)
        if result ==1:
            print ('too low , guest again')
        if result ==2:
            print ('too high, guest again')

    print ('congrats,you have geasted the number {random_number} correctly')

def check_number (guess,corect_number):
    if guess == corect_number:
        return 0
    if guess < corect_number:
        return 1
    if guess > corect_number:
        return 2



higher_numbr= input ('insert number ')
guess (higher_numbr)
