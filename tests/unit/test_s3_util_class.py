from python_poetry_template.s3_util_class import S3Util

from mock import MagicMock


def test_list_objects__when_no_objects_in_bucket__should_return_empty_list():
    # Arrange
    # Mock the s3_client with a return value on chained method calls
    mock_s3_client = MagicMock()
    mock_s3_client.get_paginator().paginate().build_full_result.return_value = {"Contents": []}
    # This also works:
    # mock_s3_client.get_paginator.return_value.paginate.return_value.build_full_result.return_value = {"Contents": []}

    # Act
    s3_util = S3Util(mock_s3_client)
    result = s3_util.list_objects("my-bucket")
    # print(f'calls: {mock_s3_client.mock_calls}')

    # Assert
    assert [] == result


def test_list_objects__when_multi_obj_in_bucket__should_return_multi_obj():
    # Arrange
    # Mock the s3_client with a return value on chained method calls
    mock_s3_client = MagicMock()
    mock_s3_client.get_paginator().paginate().build_full_result.return_value = {
        "Contents": [{"key": "some_key_value"}, {"key2": "some_key_value2"}]
    }
    # This also works:
    # mock_s3_client.get_paginator.return_value.paginate.return_value.build_full_result.return_value = {"Contents": []}

    # Act
    s3_util = S3Util(mock_s3_client)
    result = s3_util.list_objects("my-bucket")

    # Assert
    assert [{"key": "some_key_value"}, {"key2": "some_key_value2"}] == result
