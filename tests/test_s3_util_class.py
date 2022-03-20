from python_poetry_template.s3_util_class import S3Util

from mock import Mock, patch


@patch("python_poetry_template.s3_util_class.boto3")
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
    s3_util = S3Util()
    result = s3_util.list_objects("my-bucket")

    # Assert
    assert [] == result


@patch("python_poetry_template.s3_util_class.boto3")
def test_list_objects__when_multi_obj_in_bucket__should_return_multi_obj(mock_boto3):
    # Arrange

    page_object = Mock()
    page_object.build_full_result.return_value = {"Contents": [{"key": "some_key_value"}, {"key2": "some_key_value2"}]}

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
    s3_util = S3Util()
    result = s3_util.list_objects("my-bucket")

    # Assert
    assert [{"key": "some_key_value"}, {"key2": "some_key_value2"}] == result
