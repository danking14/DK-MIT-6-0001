# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2\words.txt"


def load_words():
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
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all(item in letters_guessed for item in list(secret_word))


def get_guessed_word(secret_word, letters_guessed):
    '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''
    secret_word_list = list(secret_word)
    underscore_list = ["_" for x in range(len(secret_word_list))]

    for i, char in enumerate(secret_word_list):
        if char in letters_guessed:
            underscore_list[i] = char
    current_progress = " ".join(underscore_list)
    # I made the design decision to not only present the "_"s with a space, but all the characters.
    # I think it looks nicer.

    return current_progress


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining_letters = []
    for letter in list(string.ascii_lowercase):
        if letter not in letters_guessed:
            remaining_letters.append(letter)
    return "".join(remaining_letters)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    def check_char(char):
        return char == "_" or char == " "

    no_space = my_word.replace(" ", "")
    if len(no_space) != len(other_word):
        return False
    for i, char in enumerate(no_space):
        if check_char(char):
            continue
        else:
            if char != other_word[i]:
                return False
    return True


        
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    
    matching_words = [word for word in wordlist if match_with_gaps(my_word, word)]
    print("Possible matches:", matching_words)

def hangman(secret_word):
    # TO DO
    # Add Vowel Rules (+2 for incorrect vowel)
    # Adjust warning rules so player loses guesses if they lose warnings.
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    def check_vowel(x):
        '''
        x is a single lowercase char
        Returns True if x is vowel (or "y") and False if Consonant
        '''
        return (x in "aeiouy")

    number_of_guesses = 6
    warnings = 3
    letters_guessed = []
    current_progress = ""

    print("Welcome to Hangman")
    print(f"I am thinking of a word that has {len(secret_word)} letters")
    print(f"You have {warnings} warnings left.\n----------")
    while True:
        letters_remaining = get_available_letters(letters_guessed)

        print(f"You have {number_of_guesses} guesses left.")
        print("Available letters: ", letters_remaining)
        guess = input("Please guess a letter: ").lower()
        if warnings > 0:
          
          if guess == "":
            continue
          if guess == "*":
            if show_possible_matches(current_progress) == None:
              print("No Possible Matches")
              continue
            else:
              show_possible_matches(current_progress)
            continue
            
          if guess not in string.ascii_lowercase:
              warnings -= 1
              print(f"Oops! That's not a letter. You now have have {warnings} warning/s: {current_progress}")              
              continue

          elif guess in letters_guessed:
              warnings -= 1
              print(f"Oops! You've already guessed that letter. You have {warnings} warning/s left.")
              continue
        else:
            print(f"You have entered incorrectly too many times - I warned you 3 times. Now you lose a guess")
            number_of_guesses -= 1
            continue
          


        letters_guessed.append(guess)
        current_progress = get_guessed_word(secret_word, letters_guessed)
        if guess in list(secret_word):
            print(f"Good Guess:, {current_progress}")
        else:
            print(f"Oops! That letter is not in my word: , {current_progress}")
            if check_vowel(guess):
                number_of_guesses -= 2
            else:
                number_of_guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won!\n {current_progress}")
            print(f"Your total score is {len(set(secret_word)) * number_of_guesses}")
            break
          
        if number_of_guesses == 0:
            print(f"GAME OVER! The word was {secret_word}")
            break
        print("------------------------")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
