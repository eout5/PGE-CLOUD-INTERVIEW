import boto3

client = boto3.client('cognito-idp')

response = client.create_user_pool(
    PoolName='MyUserPool'
    # Add more configuration parameters as needed
)

# Store the user pool ID for future use
user_pool_id = response['UserPool']['Id']
