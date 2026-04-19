import json
import boto3
from datetime import datetime

# Add region_name here to match your DynamoDB table location
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    try:
        method = event['httpMethod']

        if method == 'POST':
            body = json.loads(event['body'])
            if 'id' not in body:
                return response(400, "Missing student id")
            item = {
                'id': body['id'],
                'timestamp': datetime.now().isoformat(),
                'data': body
            }
            table.put_item(Item=item)
            return response(200, "Student added")

        elif method == 'GET':
            res = table.scan()
            return response(200, res['Items'])

        elif method == 'PUT':
            body = json.loads(event['body'])
            table.update_item(
                Key={
                    'id': body['id'],
                    'timestamp': body['timestamp']
                },
                UpdateExpression="set #d=:d",
                ExpressionAttributeNames={'#d': 'data'},
                ExpressionAttributeValues={':d': body}
            )
            return response(200, "Student updated")

        elif method == 'DELETE':
            body = json.loads(event['body'])
            table.delete_item(
                Key={
                    'id': body['id'],
                    'timestamp': body['timestamp']
                }
            )
            return response(200, "Student deleted")

        else:
            return response(400, "Invalid method")

    except Exception as e:
        return response(500, str(e))

def response(status, body):
    return {
        'statusCode': status,
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps(body)
    }