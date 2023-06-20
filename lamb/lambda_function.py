import boto3
import json
from custom_encoder import CustomEncoder
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
computerPath = '/computer'
computersPath = '/computers'

def lambda_handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == getMethod and path == healthPath:
        response  = buildResponse(200)
    elif httpMethod == getMethod and path == computerPath:
        response = getComputer(event['queryStringParameter']['serial'])
    elif httpMethod == getMethod and path == computersPath:
        response = getComputers()
    elif httpMethod == postMethod and path == computerPath:
        response = saveComputer(json.loads(event['body']))
    elif httpMethod == patchMethod and path == computerPath:
        request = json.loads(event['body'])
        response = modifyComputer(requestBody['serial'], requestBody['updateKey'], requestBody['updateValue'])
    elif httpMethod == deleteMethod and path == computerPath:
        request = json.loads(event['body'])
        response = deleteComputer(requestBody['serial'])
    else:
        response = buildResponse(404, 'Not Found')
    
    return response

def getComputer(serial):
    try:
        response = table.get_item(
            Key={
                'serial': serial
            }
        )
        if 'Item' in response:
            return buildResponse(200, response['Item'])
        else:
            return buildResponse(404, {'Message': 'serial: %s not found' % serial})
    except:
        logger.exception('Do your customer error handling out of her. im just gonna log it out of here!!')

def getComputers():
    try:
        response = table.scan()
        result = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
            result.extend(response['Items'])
        
        body = {
            'computers': result
        }
        return buildResponse(200, body)
    except:
        logger.exception('Do your customer error handling out of her. im just gonna log it out of here!!')

def saveComputer(requestBody):
    try:
        table.put_item(Item = requestBody, ConditionExpression='attribute_not_exists(Serial) AND attribute_not_exists(Name)')
        body = {
            'Operation': 'SAVE',
            'Message':  'SUCCESS',
            'Item': requestBody
        }
        
        return buildResponse(200, body)
    except:
        logger.exception('Do your customer error handling out of her. im just gonna log it out of here!!')
        return buildResponse(500, body = {
            'message': 'Stinky Boy'
        })

def modifyComputer(serial, updateKey, updateValue):
    try:
        response = table.update_item(
            Key = {
                'serial': serial
            },
            UpdateExpression = 'set %s = :value' % updateKey,
            ExpressionAttributeValues = {
                'value': updateValue
            },
            ReturnValues = 'UPDATED_NEW'
        )
        body = {
            'Operation': 'UPDATE',
            'Message': 'SUCCESS',
            'UpdatedAttributes': response
        }
        return buildResponse(200, body)
    except:
        logger.exception('Do your customer error handling out of her. im just gonna log it out of here!!')

def deleteComputer(serial):
    try:
        repsonse = table.delete_item(
            Key={
                'serial': serial
            },
            ReturnValues = 'ALL_OLD'
        )
        body = {
            'Operation': 'DELETE',
            'Message': 'SUCCESS',
            'deletedItem': response
        }
        return buildResponse(200, body)
    except:
        logger.exception('Do your customer error handling out of her. im just gonna log it out of here!!')

def buildResponse(statusCode, body=None):
    repsonse = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        repsonse['body'] = json.dumps(body, cls=CustomEncoder)
    return repsonse
