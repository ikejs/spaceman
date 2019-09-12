import random
import sys
import time

def printFlush(text):
   for c in text:
       print(c, end='')
       sys.stdout.flush()
       time.sleep(0.009)

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
    return ''.join(display_word)


    pass


def is_guess_in_word(guess, secret_word, not_yet_guessed):
    # Check if the letter guess is in the secret word
    if guess in secret_word:
        if guess in not_yet_guessed:
            return True
    elif guess not in secret_word:
            return False
    else:
        return False

    pass


def spaceman(secret_word):
    guesses_left = len(secret_word)
    letters_guessed = []
    not_yet_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #TODO: show the player information about the game according to the project spec
    printFlush(chr(27) + "[2J")
    printFlush('Welcome to Spaceman!\n')
    printFlush('The secret word contains: ' + str(len(secret_word)) + ' letters.\n')
    printFlush('You have ' + str(guesses_left) + ' incorrect guesses, please enter 1 letter per round.\n')
    printFlush(get_guessed_word(secret_word, letters_guessed) + '\n')
    while guesses_left > 0:
        guess = input('\nEnter a letter: ')
        # Error handle stretch challenge
        assert(len(guess) > 0), "Guess was empty!"
        print(chr(27) + "[2J")
        if guess not in letters_guessed:
            if is_guess_in_word(guess, secret_word, not_yet_guessed):
                letters_guessed.append(guess)
                not_yet_guessed.remove(guess)
                print("\nYou haven't guessed: " + ''.join(not_yet_guessed))
                print('You have ' + str(guesses_left) + ' incorrect guesses left\n')
                printFlush(get_guessed_word(secret_word, letters_guessed) + '\n')
            else:
                letters_guessed.append(guess)
                not_yet_guessed.remove(guess)
                guesses_left -= 1
                printFlush(get_guessed_word(secret_word, letters_guessed) + '\n')
                if guesses_left == 0:
                    print('Game Over! The word was: ' + secret_word)
                    if input("Do you want to play again? (Y/N): ").lower() == 'y':
                        letters_guessed = []
                        not_yet_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                        spaceman(load_word())
                else:
                    print("You haven't guessed: " + ' '.join(not_yet_guessed) + '\n')
                    print('Sorry your guess was not in the word, try again!\n')
                    print('You have ' + str(guesses_left) + ' incorrect guesses left\n')
            if is_word_guessed(secret_word, letters_guessed):
                printFlush('You Win!\n')
                guesses_left = 0
        else:
            print('Already guessed that!\n')
            print('You have ' + str(guesses_left) + ' incorrect guesses left\n')
            printFlush(get_guessed_word(secret_word, letters_guessed) + '\n')
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
spaceman(load_word())
