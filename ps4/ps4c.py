# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'ps4\words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # INPUT VALIDATION
        for vowel in VOWELS_LOWER:
            assert vowel in vowels_permutation, "enter a valid lowercase vowel"

        vowels_permutation_upper = vowels_permutation.upper()  # creates 2nd upper string
        sub_dict = {}

        for letter in (CONSONANTS_UPPER):
            # add each upper with shifted value
            sub_dict[letter] = letter

        for letter in (CONSONANTS_LOWER):
            # add each upper with shifted value
            sub_dict[letter] = letter

        for i, letter in enumerate(vowels_permutation_upper):
            sub_dict[letter] = VOWELS_UPPER[i]

        for i, letter in enumerate(vowels_permutation):
            sub_dict[letter] = VOWELS_LOWER[i]
        return sub_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypt_message = ''

        for char in self.message_text:
            if char in transpose_dict:
                encrypt_message += transpose_dict[char]
            else:
                encrypt_message += char

        return encrypt_message


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    

        Hint: use your function from Part 4A
        '''
        words = self.get_valid_words()

        max = 0
        for permutation in get_permutations("aeiou"):
            trans_dict = self.build_transpose_dict(permutation)
            decrypted_message = self.apply_transpose(trans_dict)
            decrypted_words = decrypted_message.split()
            count_valid_words = sum(
                1 for word in decrypted_words if is_word(words, word))
            if count_valid_words > max:
                max = count_valid_words
                best_message = decrypted_message
        return best_message


if __name__ == '__main__':
    def Provided_Test_Cases():
        # Example test case
        message = SubMessage(
            "Hello World! This is a test to see if this code works as intended.")
        permutation = "eaiuo"
        enc_dict = message.build_transpose_dict(permutation)
        print("Original message:", message.get_message_text(),
              "Permutation:", permutation)
        print("Expected encryption:",
              "Hallu Wurld! This is e tast tu saa if this cuda wurks es intandad")
        print("Actual encryption:", message.apply_transpose(enc_dict))
        enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
        print("Decrypted message:", enc_message.decrypt_message())

    def my_tests():
        def Submessage_unit_tests():
            message = SubMessage("Hello World")
            ### get_message_text###
            assert (message.get_message_text() == "Hello World")
            ### get_valid_words###
            assert (len(message.get_valid_words()) == 55901)

            ### build_transpose_dict###
            vowels_perm = "uoeia"
            transpose_dict = message.build_transpose_dict(vowels_perm)
            expected_mappings = {
                "U": "A",
                "O": "E",
                "E": "I",
                "I": "O",
                "U": "A",
                "u": "a",
                "o": "e",
                "e": "i",
                "i": "o",
                "u": "a"
            }
            for key, value in expected_mappings.items():
                assert transpose_dict[key] == value

            # apply_transpose
            enc_message = message.apply_transpose(transpose_dict)
            assert (enc_message == "Hille Werld")

            # decrypt_message
            enc_message = EncryptedSubMessage("Hille Werld")
            decode = enc_message.decrypt_message()
            assert (decode == "Hello World")

        # Unit Tests here
        Submessage_unit_tests()
        Provided_Test_Cases()

    my_tests()
    # TODO: WRITE YOUR TEST CASES HERE
