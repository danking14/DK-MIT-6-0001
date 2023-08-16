# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
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


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("ps4\story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###


WORDLIST_FILENAME = 'ps4\words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        

        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        import string

        # doubled both so we have space to shift to so long as < 26
        uppercase = string.ascii_uppercase + string.ascii_uppercase
        lowercase = string.ascii_lowercase + string.ascii_lowercase

        shift_dict = {}  # empty dict

        # can only do up to 26 otherwise out of bounds when shift applied
        for i, letter in enumerate(uppercase[:26]):
            # add each upper with shifted value
            shift_dict[letter] = uppercase[i+shift]

        # can only do up to 26 otherwise out of bounds
        for i, letter in enumerate(lowercase[:26]):
            # add each lower with shifted value
            shift_dict[letter] = lowercase[i+shift]

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_message = ''  # empty str to store shifted message
        # builds the shifted dict with the build_shift_dict method.
        shift_dict = self.build_shift_dict(shift)

        for char in self.message_text:
            shift_message += shift_dict.get(char, char)

        return shift_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        # self.message_text inherited
        # self.valid_words inherited
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        # self.message_text inherited
        # self.valid_words inherited

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # for shift in range_26
        # build a dict
        # apply dict with every possible shift
        # compare words to valid words
        # count valid words and apply it to a max variable
        # return tuple of (shift, message)
        max_valid_words = 0
        best_shift = 0
        words = self.get_valid_words()

        for shift in range(26):
            decoded_message = self.apply_shift(shift)
            decoded_words = decoded_message.split()
            count_valid_words = sum(
                1 for word in decoded_words if is_word(words, word))

            if count_valid_words > max_valid_words:
                max_valid_words = count_valid_words
                best_shift = shift
        decrypted_message = self.apply_shift(best_shift)
        # Corrected: return decrypt_shift
        return (best_shift, decrypted_message)


if __name__ == '__main__':

    def TestCases():

        # Test Message.apply_shift 1
        plain = Message("abc")
        cipher = plain.apply_shift(1)
        assert (cipher == "bcd")

        # Test Message.apply_shift 26
        plain = Message("zzz")
        cipher = plain.apply_shift(26)
        assert (cipher == "zzz")

        # Test Message.apply_shift punctuation and spaces
        plain = Message("! a ! 2")
        cipher = plain.apply_shift(1)
        assert (cipher == "! b ! 2")

        # Test Plaintextmessage.get_shift
        x = PlaintextMessage("abc", 1)
        y = x.get_shift()

        # Test Plaintextmessage.get_message_text_encrypted
        cipher = x.get_message_text_encrypted()
        assert (y == 1)
        assert (cipher == "bcd")

        # Test Plaintextmessage.change_shift
        x.change_shift(2)
        y = x.get_shift()
        assert (y == 2)

        # Test CiphertextMessage.decrypt_message
        x = CiphertextMessage("Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr oqzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu.")
        assert (x.decrypt_message() == (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.'))

    TestCases()

    pass  # delete this line and replace with your code here
