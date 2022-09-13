from python_poetry_template import main

from mock import patch, MagicMock


@patch("python_poetry_template.main.list_objects")
def test_get_specific_bucket_objects__when_no_objects_in_bucket__should_return_empty_list(
    mock_list_objects,
):
    # Arrange
    mock_list_objects.return_value = []

    # Act
    result = main.get_specific_bucket_objects()

    # Assert
    print(f"mock_s3_util: {mock_list_objects.call_args_list}")
    assert [] == result


@patch("python_poetry_template.main.list_objects")
def test_get_specific_bucket_objects__when_one_object_in_bucket__should_return_list_with_one_object(
    mock_list_objects,
):
    # Arrange
    mock_list_objects.return_value = [{"key": "some_object_key"}]

    # Act
    result = main.get_specific_bucket_objects()

    # Assert
    print(f"mock_s3_util: {mock_list_objects.call_args_list}")
    assert [{"key": "some_object_key"}] == result


@patch("python_poetry_template.main.S3Util.__init__")
@patch("python_poetry_template.main.S3Util.list_objects")
def test_get_specific_bucket_objects_using_util_class__when_one_object_in_bucket__should_return_list_with_one_object(
    mock_list_objects, mock_s3util_init
):
    # Arrange
    mock_s3util_init.return_value = None
    mock_list_objects.return_value = [{"key": "some_object_key"}]

    # Act
    result = main.get_specific_bucket_objects_using_util_class()

    # Assert
    print(f"mock_s3_util: {mock_list_objects.call_args_list}")
    assert [{"key": "some_object_key"}] == result


def test_get_bucket_contents_and_get_table_details_from_clients__when_bucket_exists_and_able_exists__should_return_correctly():
    # Arrange
    # Mock the s3_client with a return value on chained method calls
    mock_s3_util = MagicMock()
    mock_s3_util.list_objects.return_value = ["Some Object", "Another Object"]
    mock_dynamo_util = MagicMock()
    mock_dynamo_util.describe_table.return_value = {"TableName": "string"}

    # Act
    r = main.get_bucket_contents_and_get_table_details_from_clients(mock_s3_util, mock_dynamo_util)

    # Assert
    print(f"Calls to mock_s3_util: {mock_s3_util.list_objects.call_args_list}")
    mock_s3_util.list_objects.assert_called_with('garretts-sample-bucket')
    mock_dynamo_util.describe_table.assert_called_with("garretts-sample-table")
    assert (["Some Object", "Another Object"], {"TableName": "string"}) == r
