import random

letters_guessed = ['e']

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    # Loop through the letters in the secret_word and check if a letter is not in letters_guessed
        # https://www.programiz.com/python-programming/methods/set/issuperset
    return set(letters_guessed).issuperset(set(secret_word))

    pass

def get_guessed_word(secret_word, letters_guessed):
    display_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            display_word.append(letter+' ')
        else:
            display_word.append('_ ')

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
spaceman(load_word())
