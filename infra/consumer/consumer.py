import json 
import boto3 
import time 
from kafka import KafkaConsumer

# INITIALIZE THE CONSUMER
s3 = boto3.client(
    "s3",
    endpoint_url = "http://localhost:9002",
    aws_access_key_id = "admin",
    aws_secret_access_key = "password123"
)

bucket_name = "bronze-transactions"

# DEFINE THE CONSUMER 
consumer = KafkaConsumer(
    "stock-quotes",
    bootstrap_servers = ["localhost:9092"],
    enable_auto_commit = True, # only to say take new file only
    auto_offset_reset = "earliest", # old files will be considered also
    group_id = "bronze-consumer1",
    value_deserializer = lambda v: json.loads(v.decode("utf-8")) # conver back to python dict
)

print("We are here, streaming and saving to minio...")

#main function 
for message in consumer:
    record = message.value
    symbol = record.get('symbol')
    ts = record.get("fetched_at", int(time.time()))
    key = f"{symbol}/{ts}.json"

    s3.put_object(
        Bucket = bucket_name,
        Key = key,
        Body= json.dumps(record),
        ContentType ="application/json"
    )

    print(f"Saved record for {symbol} = s3://{bucket_name}/{key}")