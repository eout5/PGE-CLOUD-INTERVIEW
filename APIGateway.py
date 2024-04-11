import boto3

# Initialize AWS services
session = boto3.Session(region_name='YOUR_AWS_REGION')
apigateway_client = session.client('apigateway')

# Define API name and description
api_name = 'NotesAPI'
api_description = 'API for managing notes'

# Create REST API
api_response = apigateway_client.create_rest_api(name=api_name, description=api_description)
api_id = api_response['id']

# Define API resources and methods
resource_name = 'notes'
method = 'POST'  # For example, POST method for creating a note

# Create API resource
resource_response = apigateway_client.create_resource(restApiId=api_id, parentId='root', pathPart=resource_name)
resource_id = resource_response['id']

# Create API method
method_response = apigateway_client.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod=method,
    authorizationType='NONE',  # You can change this to AWS_IAM for AWS IAM authorization
)

# Create integration between API Gateway and Lambda function
lambda_function_name = 'YOUR_LAMBDA_FUNCTION_NAME'
integration_response = apigateway_client.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod=method,
    type='AWS',
    integrationHttpMethod='POST',
    uri=f'arn:aws:apigateway:{session.region_name}:lambda:path/2015-03-31/functions/arn:aws:lambda:{session.region_name}:{session.client("sts").get_caller_identity().get("Account")}:function:{lambda_function_name}/invocations'
)

# Deploy the API
deployment_response = apigateway_client.create_deployment(
    restApiId=api_id,
    stageName='prod'
)

# Get the base URL of the deployed API
base_url = f'https://{api_id}.execute-api.{session.region_name}.amazonaws.com/prod/{resource_name}'

print("API created successfully.")
print("Base URL:", base_url)
