def build_shift_dict(shift):
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
    
    upperletters = string.ascii_uppercase + string.ascii_uppercase #doubled letters to not go out of bounds, note limits shift of <26
    lowerletters = string.ascii_lowercase + string.ascii_lowercase #doubled letters to not go out of bounds, note limits shift of <26
    punctuation = string.punctuation #will this work the way I think it will?
    dictionary = {} #empty dict to kick things off
    
    for i, letter in enumerate(upperletters[:26]):
        dictionary[letter] = upperletters[i+shift] # for every letter in the alphabet, shift the key to the right by shift
        
    for i, letter in enumerate(lowerletters[:26]):
        dictionary[letter] = lowerletters[i+shift] # as above

    for punc in punctuation:
        dictionary[punc] = punctuation #punctuation should not shift
    
    return dictionary


assert(build_shift_dict(1)["a"]) == "b"
assert(build_shift_dict(26)["a"]) == "a"