from bucket_utils import get_s3_client

s3 = get_s3_client()

def apply_lifecycle_policy(bucket_name):
    lifecycle_policy = {
        'Rules': [{
            'ID': 'DeleteOldFiles',
            'Prefix': '',
            'Status': 'Enabled',
            'Expiration': {'Days': 30}
        }]
    }
    s3.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_policy
    )
    print(f"🕒 Lifecycle rule applied to {bucket_name}")