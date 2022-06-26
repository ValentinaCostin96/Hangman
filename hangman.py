######################
#
# Author: Valentina Costin
# Project: Hangman game
#
#######################


import random 
import string
from words import words 

def hangman():
    lives = 6
    word = random.choice(words).upper()
    # print('The word is: ', word)
    word_letter = set(word) #letters in the word
    alfabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed 

    while (len(word_letter) > 0 and lives > 0):
        # letter used 
        print('You have used these letters: ',''.join(used_letters))
        
        # what current word is 
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')

        print('------------ Curent word: ', word_list)

        print('Current word: ', ' '.join(word_list))

        # getting user input 
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alfabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                print('OK')
                word_letter.remove(user_letter)
            else:
                print(f'Sorry, wrong letter! \n ------------------You have {lives} left--------------')
                lives = lives - 1
        else:
            print('Nothing')
    if lives == 0:
        print(f"The word was {word}")
    else:
        print('Congratulation! You won')


if __name__ == '__main__':
    hangman()  
