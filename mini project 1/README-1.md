# Hangman Game

A simple text-based Hangman game in Python. The computer picks a random word and the player guesses it one letter at a time.

**Author:** Pratyush Singh

---

## Features

- 5 predefined words, one chosen at random
- Maximum of 6 incorrect guesses
- Input validation: only single letters are accepted, repeated guesses are ignored
- Shows word progress, wrong guesses left, and letters guessed so far
- Win and lose messages, with an option to play again

## Concepts Used

`random` module, `while` loop, `if-else`, strings, lists, functions

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

1. Keep `hangman.py` in a folder.
2. Open a terminal in that folder.
3. Run:

```
python hangman.py
```

If `python` is not recognized, use `py hangman.py`.

## Sample Output

```
=== HANGMAN ===
Guess the word! You can make 6 wrong guesses.

_ _ _ _ _ _
Wrong guesses left: 6
Guessed so far: -
Enter a letter: p
Correct!

p _ _ _ _ _
Wrong guesses left: 6
Guessed so far: p
Enter a letter: z
Wrong!
```

## How It Works

1. A random word is picked from the list.
2. The word is shown with underscores for letters not yet guessed.
3. Each guess is checked: correct letters are revealed, wrong ones reduce the remaining chances.
4. The game ends when the whole word is guessed (win) or 6 wrong guesses are used (lose).

## Files

```
task1_hangman/
├── README.md
└── hangman.py
```
