
import random
from pathlib import Path

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 6

# Locate the provided English words file in the same folder
WORD_FILE = Path(__file__).parent / "google-10000-english-no-swears.txt"

# ASCII gallows stages (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def load_words():
    """Load English words from the provided TXT file."""
    try:
        with open(WORD_FILE, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
                and line.strip().isascii()
                and len(line.strip()) >= 3
            ]

        if not words:
            raise ValueError("The English word list is empty or invalid.")

        return words

    except FileNotFoundError:
        print("\nERROR: English word list not found!")
        print(f"Please place the file here:\n{WORD_FILE}")
        raise SystemExit(1)

    except (OSError, UnicodeError) as error:
        print(f"\nERROR: Could not read the word list: {error}")
        raise SystemExit(1)


def display_game(secret_word, guessed_letters, mistakes):
    """Display the gallows and current game progress."""
    print(HANGMAN_STAGES[mistakes])

    masked_word = " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:              ", masked_word)
    print(f"Incorrect guesses:  {mistakes}/{MAX_ATTEMPTS}")

    if guessed_letters:
        print(
            "Guessed letters:   ",
            " ".join(sorted(letter.upper() for letter in guessed_letters))
        )
    else:
        print("Guessed letters:    None")

    print("-" * 35)


def play_hangman(words):
    """Play one round of Hangman."""
    secret_word = random.choice(words)
    guessed_letters = set()
    mistakes = 0

    print("\n" + "=" * 35)
    print("       WELCOME TO HANGMAN!")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses.")
    print("Enter one English letter per guess.")

    while mistakes < MAX_ATTEMPTS:
        display_game(secret_word, guessed_letters, mistakes)

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCONGRATULATIONS! YOU WON!")
            print(f"The correct word was: {secret_word.upper()}")
            return

        guess = input("Enter your guess: ").strip().lower()

        # Validate input
        if (
            len(guess) != 1
            or not guess.isalpha()
            or not guess.isascii()
        ):
            print("Invalid input! Enter one English letter.\n")
            continue

        # Do not penalize duplicate guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess.upper()}' is in the word.\n")
        else:
            mistakes += 1
            print(f"Wrong guess! '{guess.upper()}' is not in the word.\n")

    # Show the final gallows after six incorrect guesses
    display_game(secret_word, guessed_letters, mistakes)

    print("\nGAME OVER! YOU LOST!")
    print(f"The correct word was: {secret_word.upper()}")


def main():
    """Load the word list and manage replay."""
    words = load_words()

    print(f"English words loaded successfully: {len(words)}")

    while True:
        play_hangman(words)

        again = input("\nWould you like to play again? (y/n): ")
        if again.strip().lower() != "y":
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
