import json
import base64
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    base64_data = event[0]['data']
    decoded_bytes = base64.b64decode(base64_data)
    decoded_str = decoded_bytes.decode('utf-8')
    original_event = json.loads(decoded_str)
    # print("---------------------------------------",original_event)
    # print("type---------------------------------------",type(original_event))
    data = original_event['product']
    # print("---------------------------------------",data)
    # print("type---------------------------------------",type(data))

    event_type = original_event['event_type']
    data_json = json.dumps(data)
    table = dynamodb.Table('product_tb')

    # Insert data into DynamoDB table
    if event_type == 'product_added':
        try:

            response = table.put_item(Item=data)
            print("Data inserted successfully:", response)
            return {
                'statusCode': 200,
                'body': json.dumps('Data inserted successfully')
            }
        except Exception as e:
            print("Error inserting data:", e)
            return {
                'statusCode': 500,
                'body': json.dumps('Error inserting data')
            }
    elif event_type == 'product_removed':
        try:
            print("Removing product.....")
            key_to_delete = '{' + '"product_id"' + ':' + '"' + data['product_id'] + '"' + '}'
            print("key_to_delete--------------", key_to_delete)
            key_to_delete = json.loads(key_to_delete)

            print("type(key_to_delete)--------------", type(key_to_delete))

            response = table.delete_item(Key=key_to_delete)
            print("--Response Received ---------", response)
            # print("Item deleted successfully:", response)
            return {
                'statusCode': 200,
                'body': json.dumps('Item deleted successfully')
            }
        except Exception as e:
            print("Error deleting item:", e)
            return {
                'statusCode': 500,
                'body': json.dumps('Error deleting item')
            }

    # elif event_type == 'product_quantity_changed':

    # update product_inventory
    # set quantity=10 where product_id = 'P3428'

    #     try:
    #         print("Updating product.....")

    #         key_to_update =  '{' + '"product_id"'  + ':' +  '"'  + data['product_id'] + '"'  + '}'
    #         print("key_to_update--------------",key_to_update)
    #         key_to_update = json.loads(key_to_update)

    #         print("type(key_to_delete)--------------",type(key_to_update))

    #         response = table.get_item(Key=key_to_update)
    #         print("--Response Received ---------", response )

    #         # print("Item deleted successfully:", response)
    #         return {
    #             'statusCode': 200,
    #             'body': json.dumps('Item deleted successfully')
    #         }
    #     except Exception as e:
    #         print("Error deleting item:", e)
    #         return {
    #             'statusCode': 500,
    #             'body': json.dumps('Error deleting item')
    #         }

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
