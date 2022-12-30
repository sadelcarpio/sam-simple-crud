import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')


def lambda_handler(event, context):
    order = json.loads(event['body'])  # Body is a string, so it should be parsed to JSON
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=order)
    print(response)
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }
