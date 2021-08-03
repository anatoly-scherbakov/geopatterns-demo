from geopatterns_demo.models import Method


def describe_available_methods():
    """Generate list of the methods geopatterns supports."""
    return [
        {'name': name, 'label': label}
        for name, label in Method.__members__.items()
    ]
