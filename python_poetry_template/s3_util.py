import boto3

s3_client = boto3.client("s3")


def list_objects(bucket_name, jmes_exp=None):
    paginator = s3_client.get_paginator("list_objects")
    response = paginator.paginate(
        Bucket=bucket_name, PaginationConfig={}
    ).build_full_result()
    if jmes_exp:
        response = response.search(jmes_exp)
    return response["Contents"]
