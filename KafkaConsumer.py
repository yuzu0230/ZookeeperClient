from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    "test1",
    bootstrap_servers=["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"],
    value_deserializer=lambda x: loads(x.decode("utf-8")) 
    )

for c in consumer:
    print(c.value)