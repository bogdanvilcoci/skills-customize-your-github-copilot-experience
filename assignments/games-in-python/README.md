
# 📘 Assignment: Hangman Game

**Difficulty:** Beginner

## 🎯 Objective

Build a word-guessing game where a player reveals a hidden word by guessing one letter at a time. This project brings together loops, conditionals, strings, lists, and user input in a fun, interactive program.

## 📚 Learning Objectives

By completing this assignment, you will be able to:

- Use a loop to run a game until a win or loss condition is met.
- Track guesses and compare letters in strings.
- Use conditionals to respond to correct and incorrect guesses.
- Use Python's `random` module to select a word from a list.

## ✅ Before You Begin

- Be comfortable with variables, lists, `if` statements, loops, and reading input with `input()`.
- Open [`starter-code.py`](./starter-code.py), which includes a word list and TODO markers to help you get started.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word at random from the provided list and prepare the game state before the first turn.

#### Requirements
Completed program should:

- Select a secret word from the provided `words` list using Python's `random` module.
- Track the letters the player has guessed.
- Set and track the maximum number of incorrect guesses allowed.

### 🛠️ Show Guessing Progress

#### Description
Show the player's progress after each guess, revealing correctly guessed letters while keeping the other letters hidden.

#### Requirements
Completed program should:

- Display each correctly guessed letter in its position and an underscore for each hidden letter.
- For example, if the word is `python` and the player has guessed `p` and `o`, show `p _ _ _ o _`.
- Display the number of incorrect guesses remaining.

### 🛠️ Play a Complete Round

#### Description
Ask the player to guess one letter at a time, update the game state, and finish the round when the word is revealed or the player runs out of incorrect guesses.

#### Requirements
Completed program should:

- Continue asking for guesses while the game is in progress.
- Update the guessed letters when the player makes a guess.
- Not count a repeated guess as a new incorrect guess.
- End when the player reveals the whole word or uses all allowed incorrect guesses.
- Tell the player whether they won and reveal the secret word if they lost.

Start with the word display, then add one game rule at a time. Test both a winning round and a round with incorrect guesses.
