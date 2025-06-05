from bucket_utils import get_s3_client

s3 = get_s3_client()

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=expiration
    )
    print(f"🔗 Presigned URL: {url}")
    return url