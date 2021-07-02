import logging
import boto3
from botocore.exceptions import ClientError
from os import walk

s3 = boto3.client('s3')

def upload_img(file_name):
    with open("data\\img\\{}".format(file_name), "rb") as f:
        s3.upload_fileobj(f, "cloud-movies-img", file_name)
        print(file_name + ' uploaded!!')

def upload_img_all():

    for (dirpath, dirnames, filenames) in walk("data\\img\\"):
        for file_name in filenames:
            upload_img(file_name)

if __name__ == '__main__':
    pass