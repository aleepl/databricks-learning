import logging

import boto3
from botocore.exceptions import ClientError

logging.getLogger(__name__)


class S3Bucket:
    """Encapsulates S3 bucket actions."""

    def __init__(self, bucket_name: str):
        """
        :param bucket: A Boto3 Bucket name.
        """
        self.bucket = boto3.resource("s3").Bucket(bucket_name)

    def load_bin(self, object_name: str, data: list[dict]) -> None:
        """Load a file to the bucket."""
        try:
            self.bucket.put_object(Key=object_name, Body=data)
        except ClientError as error:
            logging.exception(
                "Couldn't load file '%s' into bucket '%s'. Error message: %s",
                object_name,
                self.bucket.name,
                error,
            )

    def download_file(self):
        """Download a file from the bucket."""
        pass
