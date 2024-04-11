import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def create_note(event, context):
    data = json.loads(event['body'])
    note_id = data['note_id']
    note_content = data['content']
    table.put_item(Item={'note_id': note_id, 'content': note_content})
    return {'statusCode': 200, 'body': json.dumps('Note created successfully')}

def get_note(event, context):
    note_id = event['pathParameters']['id']
    response = table.get_item(Key={'note_id': note_id})
    if 'Item' not in response:
        return {'statusCode': 404, 'body': json.dumps('Note not found')}
    return {'statusCode': 200, 'body': json.dumps(response['Item'])}

def update_note(event, context):
    data = json.loads(event['body'])
    note_id = event['pathParameters']['id']
    note_content = data['content']
    table.update_item(Key={'note_id': note_id}, UpdateExpression='SET content = :content', ExpressionAttributeValues={':content': note_content})
    return {'statusCode': 200, 'body': json.dumps('Note updated successfully')}

def delete_note(event, context):
    note_id = event['pathParameters']['id']
    table.delete_item(Key={'note_id': note_id})
    return {'statusCode': 200, 'body': json.dumps('Note deleted successfully')}
