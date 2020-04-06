# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = True
    for i in secretWord:
        if i not in lettersGuessed:
            x = False
    return x




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    stringy = ""
    for i in secretWord:
        if i in lettersGuessed:
            stringy += i
        else:
            stringy += "_"
    return stringy




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    stringy = ""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            stringy += i
    return stringy

    
secretWord = "melody"

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    n = len(secretWord)
    nMistakes = 0
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", n ,"letters long.")
    while isWordGuessed(secretWord,lettersGuessed) != True:
        print("You have", (8-nMistakes), "guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter:").lower()
        if guess in lettersGuessed:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess:", getGuessedWord(secretWord,lettersGuessed))
            if guess not in secretWord:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
                nMistakes += 1
        if nMistakes == 8:
            print("Sorry, you ran out of guesses. The word was ", secretWord, "." )
            break
    if isWordGuessed(secretWord,lettersGuessed) == True:
        print("Congratulations, you won!")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
