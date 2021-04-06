from io import BytesIO

import cairosvg
from PIL.Image import Image
from geopatterns import GeoPattern

from geopatterns_demo.models import Method


def geopattern(text: str, method: Method):
    """Generate geopattern and return it as PNG."""
    byte_string = GeoPattern(text, method.value).svg_string
    png_string = BytesIO(cairosvg.svg2png(byte_string))

    with open('test.png', 'wb+') as f:
        f.write(png_string.read())
