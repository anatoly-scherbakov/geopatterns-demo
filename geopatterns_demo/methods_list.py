from geopatterns_demo.models import Method


def describe_available_methods():
    """Generate list of the methods geopatterns supports."""
    return [
        {'name': model.name, 'label': model.value}
        for model in Method
    ]
