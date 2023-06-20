import boto3
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'Inventory'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE'
healthPath = '/health'
computer = '/computer'
computers = '/computers'

def lambda_handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == getMethod and path == healthPath:
        response  = buildResponse(200)

def buildResponse(statusCode, body=None):
    repsonse = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json'
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        repsonse['body'] = json.dumps(body)
    return repsonse