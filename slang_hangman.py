import random
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Number of attempts per round
INITIAL_ATTEMPTS = 10

# Word banks with TWO hints each + meanings
genz_words = {
    "no cap": {
        "hint1": "Opposite of lying",
        "hint2": "For real, seriously.",
        "meaning": "For real, seriously."
    },
    "rizz": {
        "hint1": "What you need to charm a crush 😉",
        "hint2": "Charisma, charm, romantic appeal.",
        "meaning": "Charisma, charm, or romantic appeal."
    },
    "slay": {
        "hint1": "What you do when you look amazing 💃",
        "hint2": "To do something really well or look amazing.",
        "meaning": "To do something really well or look amazing."
    },
    "bussin": {
        "hint1": "Describes really good food 🍔",
        "hint2": "Really good, usually food.",
        "meaning": "Really good, usually used for food."
    },
    "drip": {
        "hint1": "Talking about outfits or style",
        "hint2": "Cool outfit or personal style.",
        "meaning": "Cool outfit or personal style."
    },
    "sus": {
        "hint1": "Short for suspicious",
        "hint2": "Suspicious, shady.",
        "meaning": "Suspicious or shady."
    },
    "cap": {
        "hint1": "Opposite of 'no cap'",
        "hint2": "A lie, not true.",
        "meaning": "A lie; not true."
    },
    "flex": {
        "hint1": "Showing something off",
        "hint2": "To show off.",
        "meaning": "To show off or brag."
    },
    "vibe": {
        "hint1": "A mood or feeling",
        "hint2": "Mood or atmosphere.",
        "meaning": "A feeling, mood or atmosphere."
    },
    "lit": {
        "hint1": "Used when something is exciting",
        "hint2": "Exciting or amazing.",
        "meaning": "Exciting, fun, or amazing."
    },
    "bet": {
        "hint1": "Short response meaning 'okay' or 'sure'",
        "hint2": "Used to say 'okay' or 'sure'.",
        "meaning": "Used to say 'okay' or 'sure'."
    },
    "goat": {
        "hint1": "A title for the best ever",
        "hint2": "Greatest Of All Time.",
        "meaning": "Greatest Of All Time (the best)."
    }
}

genx_words = {
    "groovy": {
        "hint1": "70s slang ✌️",
        "hint2": "Great or fashionable (old-school).",
        "meaning": "Great or fashionable (old-school)."
    },
    "rad": {
        "hint1": "Short for radical",
        "hint2": "Awesome, cool.",
        "meaning": "Awesome, cool."
    },
    "bummer": {
        "hint1": "When things don’t go your way 😞",
        "hint2": "A disappointment.",
        "meaning": "A disappointment or downer."
    },
    "stoked": {
        "hint1": "When you're super excited",
        "hint2": "Excited.",
        "meaning": "Very excited or pumped."
    },
    "dude": {
        "hint1": "Common casual address",
        "hint2": "A friend or person.",
        "meaning": "A person or buddy; casual address."
    },
    "gnarly": {
        "hint1": "Used for something wild or difficult",
        "hint2": "Difficult or awesome, depending on context.",
        "meaning": "Can mean difficult/dangerous or awesome."
    },
    "cool beans": {
        "hint1": "An old playful approval phrase",
        "hint2": "That’s cool or awesome.",
        "meaning": "An expression meaning 'that's cool' or 'great'."
    },
    "legit": {
        "hint1": "Means genuine or real",
        "hint2": "Genuine, authentic.",
        "meaning": "Genuine, real, or authentic."
    },
    "wicked": {
        "hint1": "Regional slang for 'very good'",
        "hint2": "Very good (slang, regional).",
        "meaning": "Very good (often regional)."
    },
    "tight": {
        "hint1": "Means cool or well done",
        "hint2": "Cool, awesome.",
        "meaning": "Cool, tight-knit, or awesome depending on context."
    },
    "epic": {
        "hint1": "Used for something grand or large-scale",
        "hint2": "Amazing or grand.",
        "meaning": "Very impressive or grand."
    },
    "chill": {
        "hint1": "To relax or calm down",
        "hint2": "To relax; be calm.",
        "meaning": "Relaxed or to relax."
    }
}

# Hangman stages: index 0 = empty gallows (full attempts), index 10 = full figure (no attempts)
hangman_stages = [
    # 0 attempts used (10 left) - empty gallows
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    # 1 used
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    # 2 used
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    # 3 used
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    # 4 used
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    # 5 used
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    # 6 used
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    # 7 used - add some detail
    """
     +---+
     |   |
    \\O/  |
    /|\\  |
    / \\  |
         |
    =========
    """,
    # 8 used - more dramatic
    """
     +---+
     |   |
    \\O/| |
    /|\\  |
    / \\  |
         |
    =========
    """,
    # 9 used - almost done
    """
     +---+
     |   |
    \\O/_ |
    /|\\  |
    / \\  |
         |
    =========
    """,
    # 10 used - final stage
    """
     +---+
     |   |
     [X]  |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def clear_screen():
    # Cross-platform clear
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_category():
    print(Fore.CYAN + "Choose a category:")
    print("1. Gen Z / Gen Alpha Slang")
    print("2. Millennial / Gen X Slang")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        return genz_words, "Gen Z / Gen Alpha"
    elif choice == "2":
        return genx_words, "Millennial / Gen X"
    else:
        print(Fore.YELLOW + "Invalid choice, defaulting to Gen Z / Gen Alpha slang.")
        return genz_words, "Gen Z / Gen Alpha"

def play_game(words):
    word = random.choice(list(words.keys()))
    meta = words[word]
    clean_word = word.lower()
    # guessed_word should show spaces as spaces
    guessed_word = [" " if ch == " " else "_" for ch in clean_word]
    attempts = INITIAL_ATTEMPTS
    guessed_letters = []
    used_hint1 = False
    used_hint2 = False

    # scoring rules:
    # - win with no hints used => full points
    # - win with hint1 used => mid points
    # - win with both used => lower points
    print(Fore.CYAN + "\n🎮 Let's play Hangman! Guess the slang word/phrase.\n")

    while attempts > 0:
        # Determine stage index: 0 when attempts == INITIAL_ATTEMPTS, up to 10 when attempts == 0
        stage_index = INITIAL_ATTEMPTS - attempts
        stage_index = min(max(stage_index, 0), len(hangman_stages) - 1)
        print(hangman_stages[stage_index])

        print(f"Word: {Fore.GREEN}{' '.join(guessed_word)}{Style.RESET_ALL}")
        print(f"Attempts left: {Fore.YELLOW}{attempts}{Style.RESET_ALL}")
        print(f"Guessed letters: {Fore.MAGENTA}{', '.join(guessed_letters) if guessed_letters else 'None'}{Style.RESET_ALL}")

        guess = input("Guess a letter: ").lower().strip()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print(Fore.YELLOW + "⚠️ Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in clean_word:
            for i, ch in enumerate(clean_word):
                if ch == guess:
                    guessed_word[i] = guess
            print(Fore.GREEN + "✅ Good guess!")
        else:
            attempts -= 1
            print(Fore.RED + f"❌ Wrong guess! Attempts left: {attempts}")

        # Hints timing:
        # hint1 when half of initial attempts are left (e.g., 10 -> 5)
        if attempts == (INITIAL_ATTEMPTS // 2) and not used_hint1:
            print(Fore.MAGENTA + f"\n💡 Hint 1: {meta['hint1']}\n")
            used_hint1 = True

        # hint2 right before the final attempt (when attempts == 1)
        if attempts == 1 and not used_hint2:
            print(Fore.MAGENTA + f"\n💡 Hint 2: {meta['hint2']}\n")
            used_hint2 = True

        # Win condition
        if "_" not in guessed_word:
            print(Fore.GREEN + f"\n🎉 You guessed it! The slang was: '{word}'")
            print(Fore.CYAN + "Meaning: " + meta['meaning'])
            # scoring
            if not used_hint1 and not used_hint2:
                return 10
            elif used_hint1 and not used_hint2:
                return 8
            else:
                return 6

    # Loss condition: attempts exhausted
    print(hangman_stages[-1])
    print(Fore.RED + f"\n💀 Out of attempts! The word was: '{word}'")
    print(Fore.CYAN + "Meaning: " + meta['meaning'])
    return 0

def main():
    total_score = 0
    rounds_played = 0
    clear_screen()
    print(Fore.CYAN + "Welcome to Slang Hangman! 🎧🪄\n")
    while True:
        words, category_name = choose_category()
        print(Fore.CYAN + f"\nCategory chosen: {category_name}\n")
        score = play_game(words)
        rounds_played += 1
        total_score += score

        print(Fore.CYAN + f"\n🏆 Your score this round: {score}")
        print(Fore.CYAN + f"⭐ Total score: {total_score} (Rounds played: {rounds_played})")

        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
            if play_again in ("y", "n"):
                break
            print(Fore.YELLOW + "Please type 'y' or 'n'.")

        if play_again != "y":
            print(Fore.CYAN + "\nThanks for playing! Final score: " + str(total_score))
            print("Goodbye 👋")
            break
        clear_screen()

if __name__ == "__main__":
    main()
