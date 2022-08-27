class S3Util:
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def list_objects(self, bucket_name, jmes_exp=None):
        paginator = self.s3_client.get_paginator("list_objects")
        response = paginator.paginate(Bucket=bucket_name, PaginationConfig={}).build_full_result()
        if jmes_exp:
            response = response.search(jmes_exp)
        return response["Contents"]
