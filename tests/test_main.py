from unittest import mock
from python_poetry_template import __version__, s3_util
from python_poetry_template import main

from mock import patch


def test_version():
    assert __version__ == "0.1.0"


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
