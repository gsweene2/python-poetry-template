import boto3

from python_poetry_template import main, s3_util
from python_poetry_template.dynamo_util_class import DynamoUtil
from python_poetry_template.s3_util_class import S3Util

def test_get_bucket_contents_and_get_table_details_from_clients__when_real_bucket_exists_and_table_exists__should_return_correctly():
    # Arrange
    s3_util = S3Util(boto3.client('s3'))
    dynamo_util = DynamoUtil(boto3.client('dynamodb'))

    # Act
    r = main.get_bucket_contents_and_get_table_details_from_clients(s3_util, dynamo_util)

    # Assert - S3
    valid_objects = ['object1.txt', 'object2.txt', 'object3.txt']
    actual_objects = [i['Key'] for i in r[0]]
    assert valid_objects == actual_objects

    # Assert - Dymamo
    assert "garretts-sample-table" == r[1]['TableName']
