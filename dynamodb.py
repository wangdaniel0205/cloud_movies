'''
In case of confusion view aws_manual.txt


Add the following lines to the AWS credentials file to specify your access key ID and secrete key for the "db_user" profile

[dbaccess]
aws_access_key_id = [your access key ID]
aws_secret_access_key = [your secret access key ]
'''

import boto3
from pprint import pprint 
import json

session = boto3.Session(profile_name='dbaccess')    
dynamodb = session.resource('dynamodb', region_name='us-east-1' )
table = dynamodb.Table('cloud_movies')

'''
def table_scan():
    results = table.scan()
    for item in results['Items']:
        print(item)
'''

def read_json(file_name):
    # make sure if the json file is in \data
    return json.load(open('data\\{}.json'.format(file_name)))

def insert_db_item(item):
    response = table.put_item(
        Item = item
    )
    print('<INSERT> id: {} response: {}'.format(item['id'], response['ResponseMetadata']['HTTPStatusCode']))

def insert_db_item_all(items):
    for i in items:
        insert_db_item(i)

def get_db_item(id, print_option=False):
    response = table.get_item(
        Key={
            'id': id
        }
    )
    item = response['Item']
    if print_option: pprint(item)
    return item

def update_db_item(id, key, value):

    response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression="set {}=:k".format(key),
        ExpressionAttributeValues={
            ':k': value
        },
        ReturnValues="UPDATED_NEW"
    )
    print('<UPDATE ["{}"] -> {}> id: {} response: {}'.format(key, value, id, response['ResponseMetadata']['HTTPStatusCode']))

def delete_db_item(id):
    response = table.delete_item(
        Key={
            'id': id
        }
    )
    print('<DELETE> id: {} response: {}'.format(id, response['ResponseMetadata']['HTTPStatusCode']))
    pprint(response)


if __name__ == '__main__':
    items = read_json('items')
    insert_db_item_all(items)