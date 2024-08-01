# Basic Guessing Game

This project is a basic number guessing game implemented in Python. The user is asked to guess a number between 0 and a user-specified maximum number. The program provides feedback on whether the guess was too high or too low and congratulates the user upon a correct guess.

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
    docker pull aviadyarkoni/guessing-game:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -it aviadyarkoni/guessing-game
    ```

### Running Locally (Without Docker)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/basic-guess-game.git
    cd basic-guess-game
    ```

2. Run the Python script:
    ```bash
    python guess_game.py
    ```
