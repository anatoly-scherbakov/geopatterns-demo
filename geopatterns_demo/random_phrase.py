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
            # random.choice() is considered to be insecure by flake8-bandit,
            # but we're not using this for any kind of cryptographic
            # or security related purpose.
            return random.choice(lines).rstrip('\n')  # noqa: S311


def make_random_text():
    """Glues  and return a phrase from random words."""
    words_list = [
        MakeWord(file_path.value).random_word()
        for file_path in Thesaurus
    ]
    return str(' '.join(words_list))
