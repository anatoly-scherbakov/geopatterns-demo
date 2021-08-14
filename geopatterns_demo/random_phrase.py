import random

from geopatterns_demo.models import Thesaurus


class MakeWord():
    """Class forms a random word from the transmitted file."""

    def __init__(self, text_file):
        self.text_file = text_file

    def random_word(self):
        """Find random word in text file."""
        with open(self.text_file, 'r') as text:
            lines = text.readlines()
            return random.choice(lines).rstrip('\n')


def make_random_text():
    """Glues  and return a phrase from random words."""
    words_list = [MakeWord(word.value).random_word() for word in Thesaurus]
    return str(' '.join(words_list))
