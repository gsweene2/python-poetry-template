from xmlrpc import client
from python_poetry_template import s3_util

from mock import Mock, patch


@patch("python_poetry_template.s3_util.boto3")
def test_list_objects__when_no_objects_in_bucket__should_return_empty_list(mock_boto3):
    # Arrange

    page_object = Mock()
    page_object.build_full_result.return_value = {"Contents": []}

    # Iter Mock returns empty array (no objects)
    iter_mock = Mock()
    iter_mock.paginate.return_value = page_object

    # Client Mock
    client_mock = Mock()
    # Call to Paginator returns Iter Mock
    client_mock.get_paginator.return_value = iter_mock

    # Call to client returns Client Mock
    mock_boto3.client.return_value = client_mock

    # Act
    result = s3_util.list_objects("my-bucket")

    # Assert
    assert [] == result
