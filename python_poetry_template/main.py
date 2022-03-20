# Use . when importing module in flat structure
import logging

from .s3_util import list_objects


def get_specific_bucket_objects():
    bucket_name = "garretts-sample-bucket-he-doesnt-own"
    objects = list_objects(bucket_name)
    # ToDo: Logging doesn't print to stdout with poetry
    logging.info(f"Found {len(objects)} objects in {bucket_name}")
    print(f"Found {len(objects)} objects in {bucket_name}")
    return objects
