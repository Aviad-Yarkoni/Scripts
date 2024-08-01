import random

def guess(high_numbr):
    random_number = random.randint(0, high_numbr)
    is_correct = False

    while is_correct == False:
        guess = int(input(f'insert your guess number between 0 - {high_numbr}:'))
        is_correct = check_guess(guess, random_number, high_numbr)       
    print(f'congrats, you have guessed the number {random_number} correctly')

def check_guess(guess, correct_number, max_number):
    if guess == correct_number:
        return True
    if guess < correct_number:
        print('too low, guess again')
        return False
    if guess > max_number:
        print(f'too high, number greater {max_number}')
        return False
    if guess > correct_number:
        print('too high, guess again')
        return False

higher_numbr = int(input('insert number '))
guess(higher_numbr)
