# Use . when importing module in flat structure
import logging

from .s3_util import list_objects
from .s3_util_class import S3Util


def get_specific_bucket_objects():
    bucket_name = "garretts-sample-bucket-he-doesnt-own"
    objects = list_objects(bucket_name)
    # ToDo: Logging doesn't print to stdout with poetry
    logging.info(f"Found {len(objects)} objects in {bucket_name}")
    print(f"Found {len(objects)} objects in {bucket_name}")
    return objects


def get_specific_bucket_objects_using_util_class():
    bucket_name = "garretts-sample-bucket-he-doesnt-own"
    s3_util = S3Util()
    objects = s3_util.list_objects(bucket_name)
    # ToDo: Logging doesn't print to stdout with poetry
    logging.info(f"Found {len(objects)} objects in {bucket_name}")
    print(f"Found {len(objects)} objects in {bucket_name}")
    return objects
