from io import BytesIO

import boto3

from geopatterns_demo import models, settings
from geopatterns_demo.draw import geopattern


def file_to_s3(file_name: str, image: BytesIO) -> str:
    """Save file to S3 bucket & return its URL.
    Args:
        file_name (str): image file name
        image (BytesIO): image object in bytes
    Returns:
        str: url
    """
    s3 = boto3.Resource('s3')
    bucket = s3.Bucket(settings.S3_BUCKET_NAME)
    bucket.upload_fileobj(image.read(), file_name)
    return 'http://s3-{0}-.amazonaws.com/{1}/{2}'.format(
        settings.AWS_REGION,
        settings.S3_BUCKET_NAME,
        file_name,
    )


def get_url(text: str, method: models.Method) -> str:
    """Generate Geopatterns file & and starts the procedure for saving it.
    Args:
        text (str): text that we get from get request
        method: method for generate Geopatterns
    Returns:
        str: url
    """
    return file_to_s3(
        'image{0}.png'.format(hash(text)),
        image=geopattern(
            text=text,
            method=method,
        ),
    )
