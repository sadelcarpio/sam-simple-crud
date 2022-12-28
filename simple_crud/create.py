import json


def lambda_handler(event, context):
    order = json.loads(event['body'])  # Body is a string, so it should be parsed to JSON
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }
