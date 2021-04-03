import fastapi

from geopatterns_demo.models import Method

api = fastapi.FastAPI()


@api.get('/generate')
def generate(text: str, method: Method):
    """Generate and return a GeoPattern for rendering."""
