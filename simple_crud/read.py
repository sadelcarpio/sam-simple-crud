import json


def lambda_handler(event, context):
    order = {'id': 123, 'itemName': 'MacBook Pro', 'quantity': 2}
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(order)
    }
