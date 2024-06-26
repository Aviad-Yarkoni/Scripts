import random

def guess (high_numbr):
    random_number= random.randint(1,high_numbr)
    guess = 0 
    if guess == random_number:
        return 0
    if guess < random_number:
        return 1
    if guess > random_number:
        return 2



