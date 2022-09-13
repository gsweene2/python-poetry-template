# Use . when importing module in flat structure
import boto3
import logging

from .s3_util import list_objects
from .s3_util_class import S3Util
from .dynamo_util_class import DynamoUtil


def get_specific_bucket_objects():
    bucket_name = "garretts-sample-bucket"
    objects = list_objects(bucket_name)
    # ToDo: Logging doesn't print to stdout with poetry
    logging.info(f"Found {len(objects)} objects in {bucket_name}")
    print(f"Found {len(objects)} objects in {bucket_name}")
    return objects


def get_specific_bucket_objects_using_util_class():
    bucket_name = "garretts-sample-bucket"
    s3_util = boto3.client("s3")
    s3_util = S3Util(s3_util)
    objects = s3_util.list_objects(bucket_name)
    # ToDo: Logging doesn't print to stdout with poetry
    logging.info(f"Found {len(objects)} objects in {bucket_name}")
    print(f"Found {len(objects)} objects in {bucket_name}")
    return objects


def get_bucket_contents_and_get_table_details():
    # Create Clients
    s3_client = boto3.client("s3")
    s3_util = S3Util(s3_client)
    dynamo_client = boto3.client("dynamo")
    dynamo_util = DynamoUtil(dynamo_client)
    # Get bucket contents & table details
    bucket_objects = s3_util.list_objects("garretts-sample-bucket")
    table_details = dynamo_util.describe_table("garretts-sample-table")
    return bucket_objects, table_details


def get_bucket_contents_and_get_table_details_from_clients(s3_util, dynamo_util):
    # Get bucket contents & table details
    bucket_objects = s3_util.list_objects("garretts-sample-bucket")
    table_details = dynamo_util.describe_table("garretts-sample-table")
    return bucket_objects, table_details


# ## Call Function
# objects = get_specific_bucket_objects_using_util_class()
# print(f"found {len(objects)} objects in the bucket")

# # Create Clients
# s3_client = boto3.client("s3")
# dynamo_client = S3Util(s3_client)

# # Call Function
# bucket_contents, table_details = get_bucket_contents_and_get_table_details(s3_client, dynamo_client)
# print(f"Bucket contents: {len(bucket_contents)}")
# print(f"Table details: {table_details}")

# s3_util = S3Util(s3_client)
# dynamo_util = DynamoUtil(dynamo_client)
