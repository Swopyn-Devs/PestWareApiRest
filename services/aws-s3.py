import boto3


def upload_image(bucket, key, file):
    try:
        s3 = boto3.resource('s3')
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
