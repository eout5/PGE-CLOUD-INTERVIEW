# Step 1: Set up AWS Credentials programmatically
import boto3

# Replace 'YOUR_ACCESS_KEY_ID' and 'YOUR_SECRET_ACCESS_KEY' with your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
aws_region = 'us-west-2'  # Replace with your preferred AWS region

# Configure AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Step 2: Create AWS Lambda Functions for CRUD operations on notes
lambda_client = session.client('lambda')

# Define Lambda function code for creating a note
create_note_lambda_code = """
def lambda_handler(event, context):
    # Logic to create a new note in DynamoDB
    return {
        'statusCode': 200,
        'body': 'Note created successfully'
    }
"""

# Define Lambda function code for reading a note
read_note_lambda_code = """
def lambda_handler(event, context):
    # Logic to read a note from DynamoDB
    return {
        'statusCode': 200,
        'body': 'Note read successfully'
    }
"""

# Define Lambda function code for updating a note
update_note_lambda_code = """
def lambda_handler(event, context):
    # Logic to update a note in DynamoDB
    return {
        'statusCode': 200,
        'body': 'Note updated successfully'
    }
"""

# Define Lambda function code for deleting a note
delete_note_lambda_code = """
def lambda_handler(event, context):
    # Logic to delete a note from DynamoDB
    return {
        'statusCode': 200,
        'body': 'Note deleted successfully'
    }
"""

# Create Lambda functions for CRUD operations
create_note_function = lambda_client.create_function(
    FunctionName='CreateNoteFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with your IAM role ARN
    Handler='index.lambda_handler',
    Code={
        'ZipFile': create_note_lambda_code.encode()
    }
)

read_note_function = lambda_client.create_function(
    FunctionName='ReadNoteFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with your IAM role ARN
    Handler='index.lambda_handler',
    Code={
        'ZipFile': read_note_lambda_code.encode()
    }
)

update_note_function = lambda_client.create_function(
    FunctionName='UpdateNoteFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with your IAM role ARN
    Handler='index.lambda_handler',
    Code={
        'ZipFile': update_note_lambda_code.encode()
    }
)

delete_note_function = lambda_client.create_function(
    FunctionName='DeleteNoteFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with your IAM role ARN
    Handler='index.lambda_handler',
    Code={
        'ZipFile': delete_note_lambda_code.encode()
    }
)

print("Lambda functions created successfully")
