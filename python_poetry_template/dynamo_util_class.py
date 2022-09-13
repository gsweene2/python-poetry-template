class DynamoUtil:
    def __init__(self, dynamo_client):
        self.dynamo_client = dynamo_client

    def describe_table(self, table_name):
        response = self.dynamo_client.describe_table(TableName=table_name)
        return response["Table"]
