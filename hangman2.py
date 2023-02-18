import random
from words import words
import string
from hangman_visual import lives_visual_dict


 
def get_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 


    # getting the user input

    while len(word_letters) > 0:

        # letter used

        print("You have used these letters: ", ' '.join(used_letters))
        
        wordList = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))
        print('\n')        p

        user = input("Guess a letter: ").upper()
        if user in alphabet - used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)

        elif user in used_letters:
            print("You have already used that character. please try again.")
        
        else:
            print("Invalid character, Please try again.")




if __name__ == "__main__":
    hangman()

