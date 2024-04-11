AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'
Resources:
  CreateNoteFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: create_note.lambda_handler
      Runtime: python3.8
      Policies:
        - DynamoDBCrudPolicy:
            TableName: Notes
      Events:
        CreateNote:
          Type: Api
          Properties:
            Path: /notes
            Method: post
  # Add similar definitions for other Lambda functions
