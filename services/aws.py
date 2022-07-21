import boto3
from decouple import config


def upload_image(bucket, key, file):
    try:
        s3 = boto3.resource('s3', aws_access_key_id=config('AWS_KEY'), aws_secret_access_key=config('AWS_SECRET'))
        bucket = s3.Bucket(bucket)
        return bucket.put_object(
            ACL='public-read',
            Key=key,
            ContentType=file.content_type,
            Body=file.file
        )
    except Exception as error:
        print(error)
        return False


def upload_to_s3(bucket, key_name, file_object):
    try:
        s3 = boto3.resource('s3', aws_access_key_id=config('AWS_KEY'), aws_secret_access_key=config('AWS_SECRET'))
        bucket = s3.Bucket(bucket)
        return bucket.put_object(
            ACL='public-read',
            Key=key_name,
            Body=file_object
        )
    except Exception as error:
        print(error)
        return False


def upload_default_image(bucket, key, file):
    try:
        s3 = boto3.resource('s3', aws_access_key_id=config('AWS_KEY'), aws_secret_access_key=config('AWS_SECRET'))
        bucket = s3.Bucket(bucket)
        bucket.upload_file(file, key, ExtraArgs={'ACL': 'public-read'})
        return True
    except Exception as error:
        print(error)
        return False


def delete_file(bucket, key):
    try:
        s3 = boto3.resource('s3', aws_access_key_id=config('AWS_KEY'), aws_secret_access_key=config('AWS_SECRET'))
        s3.Object(bucket, key).delete()
        return True
    except Exception as error:
        return False
