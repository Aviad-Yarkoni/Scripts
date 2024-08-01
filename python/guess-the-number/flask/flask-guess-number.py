import random
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def check_guess(guess, correct_number, max_number):
    if guess == correct_number:
        return True
    if guess < correct_number:
        return 'Too low, guess again'
    if guess > max_number:
        return f'Too high, number greater than {max_number}'
    if guess > correct_number:
        return 'Too high, guess again'

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    random_number = request.form.get('random_number')
    max_number = request.form.get('max_number')

    if request.method == 'POST':
        if not random_number:
            max_number = int(max_number)
            random_number = random.randint(0, max_number)
            message = f'Guess a number between 0 and {max_number}'
        else:
            random_number = int(random_number)
            guess = int(request.form['guess'])
            max_number = int(request.form['max_number'])
            result = check_guess(guess, random_number, max_number)

            if result is True:
                message = f"Congrats, you have guessed the number {random_number} correctly! A new number has been generated."
                random_number = None  # Reset random_number to allow setting a new max_number
            else:
                message = result

    return render_template('index.html', message=message, random_number=random_number, max_number=max_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
