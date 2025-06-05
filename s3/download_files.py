from bucket_utils import get_s3_client

s3 = get_s3_client()

def download_file(bucket_name, file_key, download_path):
    try:
        s3.download_file(bucket_name, file_key, download_path)
        print(f"✅ Downloaded {file_key} to {download_path}")
    except Exception as e:
        print(f"❌ Download failed: {e}")