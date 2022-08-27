import boto3

from python_poetry_template.s3_util_class import S3Util

from mock import MagicMock


def test_list_objects__when_24_objects_in_pubgoer_bucket__should_return_24_objects():
    # Arrange
    s3_client = boto3.client("s3")

    # Act
    s3_util = S3Util(s3_client)
    result = s3_util.list_objects("www.pubgoer.me")
    # print(f'calls: {mock_s3_client.mock_calls}')

    # Assert
    assert 24 == len(result)
