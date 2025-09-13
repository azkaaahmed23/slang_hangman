# Slang Hangman

A fun **Python Hangman game** where you guess **Gen Z/Gen Alpha** or **Millennial/Gen X** slang words and phrases. Learn new slang while testing your guessing skills\!

-----

##  Features

  - Classic **Hangman gameplay** with ASCII art stages.
  - **Two slang categories** to choose from:
      - Gen Z / Gen Alpha slang
      - Millennial / Gen X slang
  - **Two-stage hint system**:
      - Hint 1: Shown at **half attempts left**
      - Hint 2: Shown **before the final attempt**
  - **Scoring system**:
      - **10 points**: Solved without hints
      - **8 points**: Solved with one hint
      - **6 points**: Solved with two hints
      - **0 points**: If you lose
  - Meanings of slang words are shown at the end of each round.
  - **Replay system** with a running scoreboard.
  - **Colorama colors** for a better terminal experience.

-----

##  Demo

```text
Choose a category:
1. Gen Z / Gen Alpha Slang
2. Millennial / Gen X Slang
Enter 1 or 2: 1

🎮 Let's play Hangman! Guess the slang word/phrase.

  +---+
  |   |
      |
      |
      |
      |
=========

Word: _ _ _ _ _
Attempts left: 10
Guessed letters: None
Guess a letter: r
✅ Good guess!

...

💡 Hint 1: What you need to charm a crush 😉

🎉 You guessed it! The slang was: 'rizz'
Meaning: Charisma, charm, or romantic appeal.

🏆 Your score this round: 8
⭐ Total score: 18 (Rounds played: 2)
```

-----

##  Requirements

  - Python 3.7+
  - **Colorama** for colored text
      - Install with `pip install colorama`

-----

##  How to Run

1.  **Clone the repo**:

    ```bash
    git clone https://github.com/yourusername/slang-hangman.git
    cd slang-hangman
    ```

2.  **Run the game**:

    ```bash
    python slang_hangman.py
    ```

-----

## Notes

  - Spaces in slang phrases (like "no cap" or "cool beans") are handled properly.
  - Slang banks include 12+ words each for both generations.
  - Meanings are always shown at the end, so you learn slang while playing.

-----

## Future Improvements

  - Add a multiplayer mode
  - Save high scores in a file
  - Add more categories (Boomer slang, memes, etc.)
  - Build a GUI version with Tkinter or PyGame
