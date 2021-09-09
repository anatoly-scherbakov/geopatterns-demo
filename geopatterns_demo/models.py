from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class Method(str, Enum):
    """Pattern generation method."""

    HEXAGONS = 'hexagons'
    OVERLAPPING_CIRCLES = 'overlapping_circles'
    OVERLAPPING_RINGS = 'overlapping_rings'
    PLAID = 'plaid'
    PLUS_SIGNS = 'plus_signs'
    RINGS = 'rings'
    SINEWAVES = 'sinewaves'
    SQUARES = 'squares'
    TRIANGLES = 'triangles'
    XES = 'xes'


class MethodDescription(BaseModel):
    """Class declares the model used for the response.

    Model used for the response in the /methods API endpoint.
    """

    name: str
    label: Method


class PhraseDescription(BaseModel):
    """Class declares the model used for the response.

    Model used for the response in the /random-phrase API endpoint.
    """

    text: str


class Thesaurus(Enum):
    """List of dictionaries with words.

    The order of variables determines the order of words in the outgoing phrase.
    """

    ADJECTIVES = Path(__file__).parent / 'dictionary/adjectives.txt'
    NOUNS = Path(__file__).parent / 'dictionary/nouns.txt'
