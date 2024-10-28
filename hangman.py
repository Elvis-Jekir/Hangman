import random
from difficulty_level import difficulty_level

word_list = difficulty_level() # word list based on the choice level
random_word = random.choice(word_list)  # Choose a random word from the list

guess_word = ['_'] * len(random_word)  # number of letters to guess
guess = []  # letters that the user has already guessed
max_guess = 10
incorrect_guesses = max_guess  # number of incorrect guesses

# loop for the game
while True:
    print("\nCurrent word:", " ".join(guess_word))
    print("Guessed letters:", ", ".join(guess))  # Displays letters the gamer already guessed
    print("Incorrect guesses remaining:", incorrect_guesses)

    letter = input("Guess a letter: ").strip().lower()


    if letter not in guess:
        guess.append(letter)  # Add the guessed letter
        correct_guess = False  # Check the letter are correct

        # Add the correct answer
        for index in range(len(random_word)):
            if random_word[index].lower() == letter:  # lower or uppercase
                guess_word[index] = random_word[index]  # update the guess word
                print(f"Good job!, '{letter}' is in the word.")
                correct_guess = True  # Mark as a correct guess


        # Checks if the letter was incorrect
        if not correct_guess:
            incorrect_guesses -= 1  # reduce the numb of guesses
            print(f"Sorry, '{letter}' is not in the word.")

    else:
        print(f"You already guessed '{letter}'.")

    if incorrect_guesses <= 0:
        print(f"Game Over! The word was: {random_word}")
        break
    elif '_' not in guess_word:
        print(f"Congratulations! You guessed the word: {random_word}")
        break
