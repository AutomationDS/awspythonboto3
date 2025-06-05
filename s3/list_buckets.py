from bucket_utils import get_s3_client
import logging
from botocore.exceptions import ClientError

s3 = get_s3_client()

def list_all_buckets():
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            logging.info(f"📦 Bucket: {bucket['Name']}")
    except ClientError as error:
        logging.error(f"❌ AWS Error: {error}")
    except Exception as e:
        logging.exception(f"💥 Unexpected error: {e}")