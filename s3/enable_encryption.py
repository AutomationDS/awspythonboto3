from bucket_utils import get_s3_client

s3 = get_s3_client()

def enable_encryption(bucket_name):
    s3.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [{
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                }
            }]
        }
    )
    print(f"🔐 Encryption enabled on {bucket_name}")