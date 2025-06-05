import logging
import boto3
from botocore.config import Config
from boto3.session import Session

logging.basicConfig(level=logging.INFO, format="%(pastime)s - %(levelness)s - %(message)s")

region_name = 'us-east-1'
custom_config = Config(
    retries={'max_attempts': 5, 'mode': 'standard'},
    connect_timeout=10,
    read_timeout=30
)

def get_s3_client():
    session = Session(region_name=region_name)
    return session.client('s3', config=custom_config)

def build_bucket_name(username: str, project: str, emp_id: int) -> str:
    return f"{username}-{project}-{emp_id}-bucket".lower()

def get_bucket_tags(username: str, emp_id: int, project: str):
    return [
        {'Key': 'Owner', 'Value': username},
        {'Key': 'EmployeeID', 'Value': str(emp_id)},
        {'Key': 'Project', 'Value': project}
    ]