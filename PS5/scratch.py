import string


def is_phrase_in(text):
    """
    Returns True if a phrase is in a body of text.

    Given some text, the trigger should fire only when each word in the phrase is present in its entirety and appears consecutively in the text, 
    separated only by spaces or punctuation. The trigger should not be case sensitive. 
    For example, a phrase trigger with the phrase "purple cow" should fire on the following text snippets:
    'PURPLE COW'
    'The purple cow is soft and cuddly.'
    'The farmer owns a really PURPLE cow.'
    'Purple!!! Cow!!!'
    'purple@#$%cow'
    'Did you see a purple cow?'


    """

    def clean_text(text):
        """

        Input text (string)
        Return cleaned_text (string) without punctuation
        """
        cleaned_text = ''.join(
            [char if char not in string.punctuation else ' ' for char in text])
        return cleaned_text

    phrase = "pURPLE cow"
    # Remove punctuation from input
    cleaned_text = clean_text(text)  # string
    clean_phrase = clean_text(phrase)  # string
    # Split into list by spaces
    split_text = cleaned_text.split()  # list

    split_phrase = clean_phrase.split()  # list
    for i in range(len(split_text) - len(split_phrase) + 1):
        print(F"{split_text[i:i+len(split_phrase)]=}")
        print(split_phrase)
        if split_text[i:i+len(split_phrase)] == split_phrase:
            return True
    return False


print(is_phrase_in("I have a !!!purple !!!cow"))
