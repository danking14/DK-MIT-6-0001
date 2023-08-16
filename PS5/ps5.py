# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

# ======================
# Data structure design
# ======================

# Problem 1


class NewsStory(object):
    '''
    Initializes a NewsStory object

    A NewsStory object has the following attributes:

    guid (string): the story's globally unique identifier
    title (string): the story's title
    description(string): the story's description
    link (string): the story's link
    pubdate (datetime): the story's publication date

    It has the following getter methods which each return the attributes of a specific instance of the class:

    get_guid(self)
    get_title(self)
    get_description(self)
    get_link(self)
    get_pubdate(self)

    '''

    def __init__(self, guid, title, description, link, pubdate):

        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2


# Define a class named PhraseTrigger that inherits from a class named Trigger


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        # Constructor to initialize the trigger with a given phrase
        # Validate and set the phrase
        assert self.validate_phrase(phrase), "Invalid phrase"
        self.phrase = phrase

    # static method used to assert that a phrase passed in does not have punctuation or spaces.
    @staticmethod
    def validate_phrase(phrase):
        """
        Validates the input phrase to ensure it doesn't contain punctuation and has no multiple spaces.
        Returns True if the phrase is valid, otherwise False.
        """
        # Check if the phrase contains any punctuation characters
        if any(char in string.punctuation for char in phrase):
            return False

        # check no digits in phrase
        if any(char in string.digits for char in phrase):
            return False

        # Check if the phrase contains multiple spaces in a row
        if '  ' in phrase:
            return False

        return True

    def get_phrase(self):
        """
        Returns the lowercase version of the phrase to make the comparison case-insensitive.
        """
        return self.phrase.lower()

    def is_phrase_in(self, text):
        """
        Returns True if the given phrase is present in a body of text.

        The trigger should fire only when each word in the phrase is present in its entirety and appears consecutively in the text, 
        separated only by spaces or punctuation. The trigger should not be case sensitive. 
        """

        # Define a nested function to clean the text by removing punctuation
        def clean_input(text):
            """
            Cleans the input text by replacing punctuation characters with spaces.
            """
            cleaned_text = ''.join(
                [char if char not in string.punctuation else ' ' for char in text])
            return cleaned_text

        # Get the phrase in lowercase
        phrase = self.get_phrase()

        # Remove punctuation from the input text and phrase
        cleaned_text = clean_input(text).lower()  # string

        # Split the cleaned text and phrase into a list of words
        split_text = cleaned_text.split()  # list
        split_phrase = phrase.split()  # list

        # Iterate over possible starting positions for the phrase in the text.
        # It is best to think of this for loop as taking a list of the phrase (split_phrase), and iteratively comparing that to a sub list inside the list that is split_text.
        # Like sliding a marking template along the list until it matches
        for i in range(len(split_text) - len(split_phrase) + 1):
            # Check if the current slice of text matches the cleaned phrase
            if split_text[i:i+len(split_phrase)] == split_phrase:
                return True  # Phrase found, trigger fires

        return False  # Phrase not found in the text, trigger doesn't fire


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4


class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


# ======================
# Filtering
# ======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines)  # for now, print it so you see what it contains!


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        # triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14),
                    yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(
                    END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    def provided_code():
        root = Tk()
        root.title("Some RSS parser")
        t = threading.Thread(target=main_thread, args=(root,))
        t.start()
        root.mainloop()

    def test_cases():
        # testcase Get_Phrase (tests capital input is OK, tests get_phrase returns lower)
        x = PhraseTrigger("PurPle cow")
        assert (x.get_phrase() == "purple cow")

        # test case is_phrase_in
        test_texts = [
            'PURPLE COW',
            'The purple cow is soft and cuddly.',
            'The farmer owns a really PURPLE cow.',
            'Purple!!! Cow!!!',
            'purple@#$%cow',
            'Did you see a purple cow?'
        ]
        for test in test_texts:
            assert (x.is_phrase_in(test))

    test_cases()
