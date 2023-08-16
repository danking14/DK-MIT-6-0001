# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
all_letters = VOWELS + CONSONANTS


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "PS3\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    def score1(word):
        lst = list(word)
        points = 0
        for char in lst:
            points += SCRABBLE_LETTER_VALUES.get(char.lower(), 0)  # Convert char to lowercase before looking up value
        return points
    
    def score2(word, n):
        wordlen = len(word)
        points = (7 * wordlen) - (3 *(n-wordlen))
        if points > 1:
            return points
        else: return 1
    if word == None or word == "":
        return 0
    else:    
        return score1(word) * score2(word,n)

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil((n / 3)))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    lst = list(word.lower())
    new_hand = dict(hand)
    for key in lst:
        
        if new_hand.get(key, 0) > 0:
            new_hand[key] = new_hand.get(key, 0) - 1
            if new_hand.get(key, 0) <= 0:
                del new_hand[key]
    return new_hand
        
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()
    word_dict = get_frequency_dict(word)  # function returns dict of letters:freq of letters

    if word in word_list:
        # Procedure for normal entries
        for letter in word:
            if letter not in hand or word_dict[letter] > hand[letter]:  # check if not in hand at all, and if in hand, make sure freq not more than letters in hand.
                return False
        return True
    
    
    else:
        # Check for wildcard character
        wildcard_index = word.find('*')

        if wildcard_index == -1:  # find function returns -1 if word not found.
            return False

        for v in VOWELS:
            word_copy = word[:wildcard_index] + v
            if wildcard_index != len(word) - 1:  # check if the wildcard char is at the end of the word (len-1 because indexing starts at 0). If it is not....
                word_copy += word[wildcard_index + 1:]  # add the remainder of the word beginning 1 char after wildcard
            if word_copy in word_list:  # just checks if the word with its new vowel is in the word list.
                return True

        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())
    

def play_hand(hand, word_list):
    total_score = 0
    hand_copy = hand.copy()

    while calculate_handlen(hand_copy) > 0:
        display_hand(hand_copy)

        uinput = input("Enter word, or '!!' to indicate that you are finished: ")

        if uinput == "!!":
            print("You have ended the hand by pressing !!.")
            break

        else:
            if is_valid_word(uinput, hand_copy, word_list):
                n = calculate_handlen(hand_copy)
                score = get_word_score(uinput, n)
                total_score += score
                print(f"{uinput} earned {score}. Total: {total_score}")
            else:
                print("That is not a valid word. Please choose another word")

            hand_copy = update_hand(hand_copy, uinput)

    print(f"Hand score: {total_score}")
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    if letter not in hand_copy:
        return False
    else:
        x = hand_copy[letter]
        del hand_copy[letter]
        
        random_letter = random.choice(all_letters) #all letters combo of vowels/letters
        
        while random_letter in hand_copy:
            random_letter = random.choice(all_letters) #loop to make sure random_letter not in hand already
            
        hand_copy[random_letter] = x #makes sure the amount of random letters is equal to the amount deleted
    return hand_copy
       
def get_total_hands():
    while True:
        total_hands_input = input("How many hands would you like to play: ")
        try:
            total_hands = int(total_hands_input)
            if total_hands > 0:
                return total_hands
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
           
            
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    #Input total number of hands
    series_score = 0
    
    

                
    total_hands_input = get_total_hands()
    total_hands = total_hands_input
    replay_flag = False
    sub_flag = False
    while total_hands > 0:
        print(f"You have {total_hands} hands left to play")
        hand = deal_hand(HAND_SIZE)
        #ask user if they went to substitute - this can only be done once per game:
        if sub_flag == False:
            display_hand(hand)
            while True:
                sub = input("Would you like to substitute a letter? yes or no: ").lower()
                
                if sub == "yes":
                    sub_flag = True
                    letter = input("Enter Letter you'd like to substitute: ")
                    
                    hand = substitute_hand(hand, letter)
                    print(f"Replaced all letter {letter}\n No more substitutions left.")
                    
                    print("Here is your new hand")
                    display_hand(hand)
                    break  # You should break the loop after substituting the letter
                elif sub == "no":
                    print("No substitution this round")
                    break  # You should also break the loop if the user doesn't want to substitute
                else:
                    print("Please enter yes or no:")
                    # If the input is neither "yes" nor "no", the loop will continue to ask for input.

        
        score = play_hand(hand, word_list)

        if replay_flag == False:
            while True:
                replay = input("Would you like to replay your hand? yes or no ")
                    
                if replay.lower() == "no":
                    print("No Replay this round")
                    break
            
                elif replay.lower() == "yes":
                    replay_flag = True
                    print("Replay used. No more replays.")
                    score = play_hand(hand, word_list)
                    break
                else:
                    print("Please enter yes or no:")
                    continue
                
        
        series_score += score
        print(f"Total Score: {series_score}")
        total_hands -= 1
    print(f"Game over - after {total_hands_input} hands, your total score is {series_score}")
    return series_score

    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
