import loremipsum


def make_random_text():
    """Method create random phrase using loremipsum library."""
    return loremipsum.generate(1, 'short')
