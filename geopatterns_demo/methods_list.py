from geopatterns_demo.models import Method

def list_creator():
    """Generate list of the methods geopatterns supports."""
    methods_list = []
    for name, label in Method.__members__.items():
        methods_list.append(
            {
                'name': name,
                'label': label
            }
        )
    return methods_list
