# Select a word(Which should be capital and not have space in between or -)
import random
from words import words
import string


def valid_world(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = valid_world(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6
    while len(word_letter) > 0 and lives > 0:
        # To print used letter
        print(f'You have {lives} lives left', 'You have used these letter: ', ' '.join(used_letter))
        # Print the letter line
        word_list = [letter if letter in used_letter else '_' for letter in word]
        print("The current word is: ", ' '.join(word_list))
        # user input
        user_input = input("Enter your letter").upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                lives = lives-1
                print("Letter in not in words")

        elif user_input in used_letter:
            print("You have already used the letter please try again")

        else:
            print("Invalid input")
    if lives == 0:
        print('You have lost the game sorry', word)
    else:
        print("You won the game congo", word)


hangman()
