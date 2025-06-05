from create_bucket import create_bucket
from delete_bucket import delete_bucket
from list_buckets import list_all_buckets
from upload_files import upload_file
from download_files import download_file
from enable_encryption import enable_encryption
from lifecycle_manager import apply_lifecycle_policy
from presigned_url import generate_presigned_url

users = [
    {'name': 'balaji', 'id': 235},
    {'name': 'pragnaysri', 'id': 1432}
]

for user in users:
    bucket_name = f"{user['name']}-webapps-{user['id']}-bucket"
    create_bucket(user['name'], user['id'])
    upload_file(bucket_name, 'test.txt')
    enable_encryption(bucket_name)
    apply_lifecycle_policy(bucket_name)
    generate_presigned_url(bucket_name, 'test.txt')
    download_file(bucket_name, 'test.txt', 'downloaded_test.txt')
    # delete_bucket(user['name'], user['id'])

list_all_buckets()