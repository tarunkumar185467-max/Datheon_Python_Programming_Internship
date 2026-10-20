
# Hangman Game 🎮

## About the Project

This is a simple, terminal-based Hangman game that I developed as part of my Python internship.

I built this project to practice Python programming and understand how concepts like loops, conditional statements, sets, and random selection work in a real application.

In this game, the computer selects a secret word, and the player tries to guess it one letter at a time. The goal is to reveal the complete word before running out of attempts.

## How to Play

1. Run the Python program in your terminal.
2. The game selects a hidden word.
3. Guess one letter at a time.
4. Correct guesses reveal the matching letters in the word.
5. Incorrect guesses reduce your remaining attempts and update the Hangman drawing.
6. You win if you guess the word before reaching six incorrect guesses.
7. If you run out of attempts, the game ends and reveals the secret word.

## Features

- Random selection of a secret word.
- A hidden-word display that updates after each guess.
- ASCII Hangman drawings that change with incorrect guesses.
- A maximum of six incorrect guesses.
- Tracking of previously guessed letters.
- Protection against duplicate guesses counting as extra mistakes.
- Clear victory and defeat messages.

## Technologies Used

- Python 3
- `random` module for selecting a secret word.
- Standard Python data structures and control statements.

## Project Structure

```text
Python_Hangman/
├── hangman.py
└── README.md
```

If the program uses an external word-list file, keep that file in the project and include it in the repository as well.

## How to Run the Game

Make sure Python is installed on your computer.

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run this command:

   ```bash
   python hangman.py
   ```

5. Follow the instructions displayed in the terminal and start guessing!

## What I Learned

While working on this project, I practised using Python's `random` module, managing guessed letters with a set, handling user input, and using loops and conditions to control the game.

I also learned how to update ASCII art according to the player's mistakes and how to prevent repeated guesses from unfairly reducing the number of remaining attempts.

This project helped me improve my problem-solving skills and gain more confidence in writing Python programs.

## Learning Resource

The following word list was suggested in the internship task and can be used if the program is designed to load words from a text file:

https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt

## Conclusion

Building this Hangman game was a useful hands-on learning experience. It helped me turn basic Python concepts into an interactive game and gave me a better understanding of how small programs can be built step by step.

This project is one of my learning milestones as I continue improving my Python programming skills.

---
