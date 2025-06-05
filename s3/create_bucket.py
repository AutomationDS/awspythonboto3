from bucket_utils import get_s3_client, build_bucket_name, get_bucket_tags, region_name
import logging
from botocore.exceptions import ClientError

s3 = get_s3_client()
project_name = 'webapps'

def create_bucket(username: str, emp_id: int):
    bucket_name = build_bucket_name(username, project_name, emp_id)
    try:
        existing_buckets = s3.list_buckets()['Buckets']
        if any(b['Name'] == bucket_name for b in existing_buckets):
            logging.info(f"✅ Bucket already exists: {bucket_name}")
            return
        logging.info(f"🚀 Creating new bucket: {bucket_name}")
        if region_name == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region_name}
            )
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': get_bucket_tags(username, emp_id, project_name)}
        )
        logging.info(f"🎉 Bucket created and tagged: {bucket_name}")
    except ClientError as error:
        logging.error(f"❌ AWS Error: {error}")
    except Exception as e:
        logging.exception(f"💥 Unexpected error: {e}")