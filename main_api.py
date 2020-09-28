import boto3

s3_client = boto3.client('s3')


# def generate_random_filename(file_name):
#     random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
#     return random_file_name


def upload_file(bucket_name, file_name, file_content):
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)


def download_file(bucket_name, file_key, file_name):
    with open('/tmp/%s' % file_name, 'wb') as data:
        s3_client.download_fileobj(bucket_name, file_key, data)

    data.close()


def list_objects(bucket_name):
    objects_list = s3_client.list_objects(Bucket=bucket_name)['Contents']

    for item in objects_list:
        print("Chave: {}".format(item['Key']))


def check_object(bucket_name, file_key):
    objects_list = s3_client.list_objects(Bucket=bucket_name)['Contents']

    for item in objects_list:
        if item['Key'] == file_key:
            print("Item encontrado!")


def get_object_info(bucket_name, file_key):
    object_info = s3_client.get_object(Bucket=bucket_name, Key=file_key)

    print(object_info)
