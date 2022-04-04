import boto3
from pydantic import BaseModel


class ResponseUpload(BaseModel):
    success: bool
    message: str


def upload_image(bucket, key, file):
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket)
        upload = bucket.put_object(
            ACL='public-read',
            Key=key,
            ContentType=file.content_type,
            Body=file.file
        )
        return ResponseUpload(upload, 'Ok')
    except Exception as error:
        print(error)
        return ResponseUpload(False, error)
