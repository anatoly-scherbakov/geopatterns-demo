from io import BytesIO

import boto3

from geopatterns_demo import models, settings
from geopatterns_demo.draw import geopattern


def hash_name(text: str) -> str:
    """Generate the file name using the hash function.

    Args:
        text (str): text that we get from get request

    Returns:
        str: file name
    """
    return 'image{0}.png'.format(hash(text))


def check_file(file_name: str, bucket: boto3) -> bool:
    """Check the file for presence in the S3 bucket.

    Args:
        file_name (str): image file name
        bucket (boto3): boto3 object - S3 bucket

    Returns:
        bool: bool
    """
    bucket_object = list(bucket.objects.filter(Prefix=file_name))
    if len(bucket_object) > 0:  # noqa: WPS507
        return bucket_object


def file_to_s3(file_name: str, image: BytesIO) -> str:
    """Save file to S3 bucket & return it's URL.

    Args:
        file_name (str): image file name
        image (BytesIO): image object in bytes

    Returns:
        str: url
    """
    s3 = boto3.Resource('s3')
    bucket = s3.Bucket(settings.S3_BUCKET_NAME)
    bucket.upload_fileobj(image.read(), file_name)
    if check_file(file_name, bucket):
        return 'http://s3-{0}-.amazonaws.com/{1}/{2}'.format(
            settings.AWS_REGION,
            settings.S3_BUCKET_NAME,
            file_name,
        )
    return 'error: file is not saving.'


def get_url(text: str, method: models.Method) -> str:
    """Generate Geopatterns file & and starts the procedure for saving it.

    Args:
        text (str): text that we get from get request
        method: method for generate Geopatterns

    Returns:
        str: url
    """
    return file_to_s3(
        hash_name(text),
        image=geopattern(
            text=text,
            method=method,
        ),
    )
