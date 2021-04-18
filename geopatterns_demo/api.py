import fastapi
from fastapi.responses import Response
from mangum import Mangum

from geopatterns_demo.draw import geopattern
from geopatterns_demo.models import Method

api = fastapi.FastAPI()


@api.get('/generate', response_class=Response)
def generate(
    text: str = fastapi.Query(..., max_length=1024),
    method: Method = Method.HEXAGONS,
):
    """Generate and return a GeoPattern for rendering."""
    image = geopattern(
        text=text,
        method=method,
    )
    return Response(
        content=image,
        media_type='image/png',
        headers={
            'Cache-Control': 'public, max-age=31536000',
        },
    )


lambda_handler = Mangum(api)
