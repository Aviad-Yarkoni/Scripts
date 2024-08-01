# Flask Guessing Game

This project is a simple number guessing game implemented using Flask. The user is asked to guess a number between 0 and a user-specified maximum number. The app provides feedback on whether the guess was too high or too low and congratulates the user upon a correct guess.

## Features

- User can set a maximum number for the guessing range.
- Provides feedback on whether the guess is too high or too low.
- Automatically generates a new number after a correct guess.

## Getting Started

### Prerequisites

- Docker

### Running with Docker

1. Pull the Docker image from Docker Hub:
    ```bash
    docker pull aviadyarkoni/flask-guess-game:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 aviadyarkoni/flask-guess-game
    ```

3. Open your browser and go to `http://localhost:5000` to start the game.
