import os
from bucket_utils import get_s3_client

s3 = get_s3_client()

def upload_file(bucket_name, file_path):
    try:
        file_key = os.path.basename(file_path)
        s3.upload_file(file_path, bucket_name, file_key)
        print(f"✅ Uploaded {file_path} to {bucket_name}/{file_key}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")