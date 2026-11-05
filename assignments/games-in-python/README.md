
# Hangman Game Challenge

**Difficulty:** Beginner

## Objective

Build a word-guessing game where the player reveals a hidden word by guessing one letter at a time. This is a chance to practice loops, conditionals, strings, lists, and user input in one small project.

## Learning Objectives

By completing this assignment, you will be able to:

- Use a loop to keep a game running until a condition is met.
- Compare strings and update a collection of guessed letters.
- Use conditionals to respond to correct and incorrect guesses.
- Use Python's `random` module to choose a word.

## Before You Begin

You should be comfortable with variables, lists, `if` statements, loops, and reading input with `input()`. The starter file includes a word list and TODO markers to help you get started.

## Tasks

### 1. Set up the game

Choose a secret word at random from the provided list. Create variables to store the letters guessed so far and the number of incorrect guesses allowed.

### 2. Show the word as it is guessed

Display each letter that has been guessed correctly and use an underscore for each hidden letter. For example, if the word is `python` and the player has guessed `p` and `o`, show `p _ _ _ o _`.

### 3. Run a complete round

Ask the player for a letter, check whether it is in the secret word, and update the game state. Continue until the player reveals every letter or runs out of incorrect guesses.

## Completion Checklist

Your game is ready when it:

- Selects one word randomly from the provided list.
- Shows correct guesses in their positions and underscores for hidden letters.
- Tracks and displays the remaining incorrect guesses.
- Does not count a repeated guess as a new incorrect guess.
- Ends when the word is complete or no incorrect guesses remain.
- Tells the player whether they won and reveals the word if they lost.

Start with the word display, then add one game rule at a time. Test both a winning round and a round with incorrect guesses.
