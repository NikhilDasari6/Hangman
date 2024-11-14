import random

# Step 1: Get a list of words from the user

# Step 2: Randomly select a word from the list
words = ["algorithm","function","variable","compile","iterate","recursion","binary","array","syntax","pointer"] 

chosen_word = random.choice(words).lower()
word_length = len(chosen_word)

# Step 3: Initialize game variables
display = ['_'] * word_length  # Display underscores for unguessed letters
attempts = 6  # Number of wrong guesses allowed
guessed_letters = []
wrong_attempts = 0

print("\nWelcome to Hangman!")
print(" ".join(display))

# Step 4: Main game loop
while attempts > 0:
    print("HANGMAN")
    pointer_position = " " * wrong_attempts + "^"  # Position the pointer based on wrong attempts
    print(pointer_position)

    guess = input("\nGuess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # Add guess to guessed letters list
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in chosen_word:
        # Reveal the guessed letters in the display
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Good guess!")
    else:
        # Deduct an attempt if guess is wrong
        attempts -= 1
        wrong_attempts += 1
        print("Wrong guess. You have", attempts, "attempts left.")

    # Show current progress
    print(" ".join(display))

    # Check if the word has been guessed
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", chosen_word)
        print("\nPhew... you are saved.")
        break
else:
    print("\nSorry, you've run out of attempts. The word was:", chosen_word)

