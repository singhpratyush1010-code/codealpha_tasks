import random

WORDS = ["python", "django", "laptop", "coding", "server"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []      # all letters guessed so far
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word! You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed so far: {', '.join(guessed) if guessed else '-'}")

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed for letter in word):
            print(display_word(word, guessed))
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
