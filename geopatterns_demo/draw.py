from io import BytesIO

import cairosvg
from geopatterns import GeoPattern

from geopatterns_demo.models import Method


def geopattern(text: str, method: Method) -> bytes:
    """Generate geopattern and return it as PNG."""
    byte_string = GeoPattern(text, method.value).svg_string
    png_string = BytesIO(cairosvg.svg2png(byte_string))
    return png_string.read()
