import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

end_of_the_game = False

chosen_word = random.choice(word_list)

word_display = list('_' * len(chosen_word))

print(logo)
print(f"{' '.join(word_display)}")

while not end_of_the_game:
    guess = input("Guess a letter:\n").lower()

    if guess in word_display:
        print(f"You've already guessed {guess}.")
    else:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[idx] = letter
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life. Lives remaining: {lives}")
            if lives == 0:
                print("You lost!")
                end_of_the_game = True

    if '_' not in word_display:
        end_of_the_game = True
        print("You won!")
        print(f"Guessed word is: {' '.join(word_display)}")

    if lives > 0:
        print(f"{' '.join(word_display)}")
        print(stages[lives])
