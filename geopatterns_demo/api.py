import typing

import fastapi
import sentry_sdk
from fastapi.responses import Response
from mangum import Mangum
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from starlette.middleware.cors import CORSMiddleware

from geopatterns_demo import methods_list, models, random_phrase, settings
from geopatterns_demo.draw import geopattern

if settings.IS_IN_LAMBDA:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[AwsLambdaIntegration()],
    )

api = fastapi.FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)


@api.get('/generate', response_class=Response)
def generate(
    text: str = fastapi.Query(..., max_length=1024),
    method: models.Method = models.Method.HEXAGONS,
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


@api.get(
    '/methods',
    response_model=typing.List[models.MethodDescription],
)
def methods():
    """Generate and return list of the methods geopatterns supports."""
    return methods_list.describe_available_methods()


@api.get(
    '/random-phrase',
    response_model=models.PhraseDescription,
)
def phrase():
    """Generate and return return random phrase."""
    return {'text': random_phrase.make_random_text()}


lambda_handler = Mangum(ap'')
