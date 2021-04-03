from geopatterns import GeoPattern

from geopatterns_demo.models import Method


def geopattern(text: str, method: Method):
    """Generate geopattern and return it as PNG."""
    return str(GeoPattern(text, method.value))
