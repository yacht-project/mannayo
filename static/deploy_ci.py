#!/usr/bin/env python3
import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()


# 아직 다른게 없으니까 index.html 만 올립니다
bucket_name = 'mannayo-test'
filename = 'index.html'

with open(filename, 'rb') as data:
    s3.put_object(
        Body=data,
        Bucket=bucket_name,
        Key=filename,
        ContentType='text/html',
        ACL='public-read',
    )
