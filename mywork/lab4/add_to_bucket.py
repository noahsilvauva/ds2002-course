#!/c/Users/nsilv/anaconda3/python.exe

import boto3
from urllib import request

url = 'https://news.virginia.edu/sites/default/files/Header_NA_MedSchoolMoney_SS.jpg'
download_file_name = "Header_NA_MedSchoolMoney_SS.jpg"

def download(url, download_file_name):
    request.urlretrieve(url, download_file_name)

download(url, download_file_name)

# create client

s3 = boto3.client('s3', region_name="us-east-1")

# specify bucket name and file

bucket = 'ds2002-acv7qc'
local_file = 'Header_NA_MedSchoolMoney_SS.jpg'
expires_in = 604800

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read'
)

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': local_file},
    ExpiresIn=expires_in
)

print(response)
