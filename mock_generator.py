import base64
import datetime
import json
import boto3
import random
import time
from faker import Faker
from decimal import Decimal

fake = Faker()
# Initialize the DynamoDB resource
# dynamodb = boto3.resource('dynamodb')
kinesis_client = boto3.client('kinesis',region_name='us-east-1')
event_types = ['product_added', 'product_removed']

# sample event
"""
{
"event_type": "product_added",
"product": {
"product_id": "P98765",
"product_name": "Laptop",
"quantity": 10,
"timestamp": "2023-09-11T12:00:00Z"
}
}

"""

# generate timestamp
def random_timestamp(start_year, end_year):
    # Generate a random year, month, day, hour, minute, second
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assume all months have 28 days for simplicity
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    # Create a datetime object with the random values
    random_datetime = datetime.datetime(year, month, day, hour, minute, second)

    return random_datetime
def generate_inventory_data():
    """Generate random order data."""
    event_type = random.choice(event_types)
    product_id = fake.unique.bothify("P#####")
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 50)
    start_year = 2022
    end_year = 2023
    timestamp = str(random_timestamp(start_year, end_year))

    return {
                "event_type": event_type,
                "product": {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity,
                "timestamp": timestamp
                }
             }


if __name__ == '__main__':
    try:
        while True:
            data = generate_inventory_data()
            # data_json = json.dumps(data)
            # print(data_json)
            # print(type(data_json))
            # print(data)
            # print(data['product']['product_id'])
            print(data)

            # Serialize the data dictionary into a JSON string
            data_str = json.dumps(data)

            # Encode the JSON string into bytes
            data_bytes = data_str.encode('utf-8')

            # # Encode the bytes to a Base64 byte string
            # encoded_data = base64.b64encode(data_bytes).decode('utf-8')

            # Use 'product_id' as the partition key
            partition_key = data ['product']['product_id']

            response = kinesis_client.put_record(
                StreamName='stream',
                Data=data_bytes,  # Data must be a base64-encoded string
                PartitionKey=partition_key
            )

            time.sleep(1)  # Sleep for 10 seconds
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")
