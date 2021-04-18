from io import BytesIO

import cairosvg
from geopatterns import GeoPattern

from geopatterns_demo.models import Method


def geopattern(text: str, method: Method) -> BytesIO:
    """Generate geopattern and return it as PNG."""
    byte_string = GeoPattern(text, method.value).svg_string
    return BytesIO(cairosvg.svg2png(byte_string))
