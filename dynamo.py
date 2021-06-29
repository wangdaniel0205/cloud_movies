import boto3

'''
Edit the credential file at ~/.aws/credentials 
(in windows, the location may be c:\\users\\[username]\\.aws\\credentials)

Add the following lines to the AWS credentials file to specify your access key ID and secrete key for the "db_user" profile

[dbaccess]
aws_access_key_id = [your access key ID]
aws_secret_access_key = [your secret access key ]
'''

session = boto3.Session(profile_name='admin')    
dynamodb = session.resource('dynamodb', region_name='us-east-1' )


def create_movie_table():  
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


movie_table = create_movie_table()
print("Table status:", movie_table.table_status)


