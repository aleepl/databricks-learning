import logging
import json
import boto3
from botocore.exceptions import ClientError
from typing import Any, Dict

logger = logging.getLogger(__name__)


class S3Bucket:
    """Encapsulates S3 bucket actions."""

    def __init__(self, bucket_name: str):
        """
        :param bucket: A Boto3 Bucket name.
        """
        self.bucket = boto3.resource("s3").Bucket(bucket_name)

    def load(self, object_name: str, data: Dict[str, Any]) -> None:
        """Load a file to the bucket."""
        try:
            body = json.dumps(data).encode("utf-8")
            self.bucket.put_object(Key=object_name, Body=body)
        except ClientError as error:
            logger.exception(
                "Couldn't load file '%s' into bucket '%s'. Error message: %s",
                object_name,
                self.bucket.name,
                error,
            )

    def download_file(self):
        """Download a file from the bucket."""
        pass
