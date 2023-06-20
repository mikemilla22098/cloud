import boto3

client = boto3.client(
    'dynamodb',
    aws_access_key_id='AKIAVD7O37KZWD2EMKQ7',
    aws_secret_access_key='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',
    region_name='us-east-2'
    )
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAVD7O37KZWD2EMKQ7',
    aws_secret_access_key='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',
    region_name='us-east-2'
    )
ddb_exceptions = client.exceptions

__TableName__ = "Inventory"
Primary_Column_Name = 'Name'
Primary_Key = '1P0730PC01'
columns=["Serial","Building"]

#DB =     boto3.resource('dynamodb')
table = dynamodb.Table(__TableName__)
def table_get():
    response = table.get_item(
                Key={
                    Primary_Column_Name:Primary_Key,
                    'Serial':'MXL15141234'
                }
            )

    item = response["Item"]
    print(item)
def add_item():
    Primary_Key = '2p0456tc01'

    response = table.put_item(
        Item={
            Primary_Column_Name:Primary_Key,
            columns[0]: '2ua76390',
            columns[1] :"MOB",
            columns[2]: "test"
                }
            )
    response["ResponseMetadata"]["HTTPStatusCode"]
#table_get()
add_item()
table_get()