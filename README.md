# 🔠 Hangman – Python Console Game

Hangman is a classic word-guessing game brought to life in your terminal!\
This project uses Python to combine logic, visuals, and interactivity in a fun and educational way.

---

## 🎮 Game Overview

- The computer picks a **random word** from a predefined list.
- Some letters are revealed, others are hidden with `_`.
- You guess one letter at a time.
- If the letter is correct, it fills in the blanks.
- If not, you lose a life — and the **Hangman gets drawn** step by step.
- You win if you guess the word before the full hangman is drawn.

---

## ✨ Features

- ✅ Random word selection
- ✅ Partially hidden word (some letters already shown)
- ✅ ASCII-based hangman drawing with 7 lives
- ✅ User input validation & repeat guess warnings
- ✅ Clean console output with feedback

---

## 📂 Project Structure

```bash
hangman/
├── hangman.py        # Main game script with all logic
├── hang_db.py        # Contains word list, stages & ASCII logo
├── Screenshot.png    # Terminal screenshot of the game running
└── README.md         # This documentation file
```

---

## 🖥️ How to Play

1. Run `hangman.py` using Python 3.
2. Guess one letter at a time.
3. Avoid losing all 7 lives!
4. Win by guessing the full word before the hangman is complete.

---

## 🔍 Sample Output

```
_ _ p _ e
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

Guessed a letter :- a
You choose correct word 'a'.

_ a p _ e
```

---

## 🚀 Run the Game

### Requirements:

- Python 3.x installed

### Run:

```bash
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
python hangman.py
```

---

## 💡 What I Learned

- Managing game state using loops and flags
- Handling user inputs cleanly
- Randomization with controlled output
- Creating visual feedback using ASCII art
- Organizing a Python project with multiple files

---

## © Author

**Created by Saurabh Kulshrestha**\
Open for suggestions and contributions!
