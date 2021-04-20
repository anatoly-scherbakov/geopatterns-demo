import fastapi
import sentry_sdk
from fastapi.responses import Response
from mangum import Mangum
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from geopatterns_demo import settings
from geopatterns_demo.draw import geopattern
from geopatterns_demo.models import Method

if settings.IS_IN_LAMBDA:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[AwsLambdaIntegration()],
    )

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
        content=image.read(),
        media_type='image/png',
        headers={
            'Cache-Control': 'public, max-age=31536000',
        },
    )


lambda_handler = Mangum(api)
