from bucket_utils import get_s3_client, build_bucket_name, region_name
import logging
from botocore.exceptions import ClientError

s3 = get_s3_client()
project_name = 'webapps'

def delete_bucket(username: str, emp_id: int):
    bucket_name = build_bucket_name(username, project_name, emp_id)
    try:
        logging.info(f"🗑️ Deleting bucket: {bucket_name}")
        s3.delete_bucket(Bucket=bucket_name)
        logging.info(f"✅ Bucket deleted: {bucket_name}")
    except ClientError as error:
        logging.error(f"❌ AWS Error: {error}")
    except Exception as e:
        logging.exception(f"💥 Unexpected error: {e}")