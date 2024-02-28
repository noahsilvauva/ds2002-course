#!/c/Users/nsilv/anaconda3/python.exe

import boto3
from urllib import request

url = "https://images.albertsons-media.com/is/image/ABS/184450056?$ng-ecom-pdp-desktop$&defaultImage=Not_Available"
download_file_name = "C:\\Users\nsilv\ds2002-course\mywork\lab4\onion.jpg"

def download(url, download_file_name):
    request.urlretrieve(url, download_file_name)

download(url, download_file_name)

# create client

s3 = boto3.client('s3', region_name="us-east-1")

# specify bucket name and file

bucket = 'ds2002-acv7qc'
local_file = 'lab4/onion.jpg'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read'
)

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': object_name},
    ExpiresIn=expires_in
