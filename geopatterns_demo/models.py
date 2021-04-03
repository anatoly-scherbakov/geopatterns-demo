from enum import Enum


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
