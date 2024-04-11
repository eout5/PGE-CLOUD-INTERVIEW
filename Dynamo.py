import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.create_table(
    TableName='Notes',
    KeySchema=[
        {
            'AttributeName': 'note_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'note_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='Notes')
