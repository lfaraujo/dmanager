import json

import boto3

from config.aws_config import AWS_CONFIG

s3_client = boto3.client('s3')


def upload_file(file_name, file_content):
    s3_client.put_object(Bucket=AWS_CONFIG['bucket_name'], Key=file_name, Body=file_content)

    return {'file_uploaded': file_name}


def download_file(file_key, directory):
    with open('%s%s' % (directory, file_key), 'wb') as data:
        s3_client.download_fileobj(AWS_CONFIG['bucket_name'], file_key, data)

    data.close()

    return {'file_downloaded': file_key}


def list_objects():
    objects_list = s3_client.list_objects(Bucket=AWS_CONFIG['bucket_name'])

    if 'Contents' in objects_list:
        return json.dumps([{'item_key': item['Key']} for item in objects_list['Contents']])


def check_object(file_key):
    objects_list = s3_client.list_objects(Bucket=AWS_CONFIG['bucket_name'])['Contents']

    for item in objects_list:
        if item['Key'] == file_key:
            return True

    return False


def get_object_info(file_key):
    object_info = s3_client.get_object(Bucket=AWS_CONFIG['bucket_name'], Key=file_key)

    print(object_info)
