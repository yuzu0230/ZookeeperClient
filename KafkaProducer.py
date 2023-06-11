from kafka import KafkaProducer
from json import dumps
import pandas as pd

# kafka settings
TOPIC_NAME = "test1"
BOOTSTRAP_SERVERS = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_serializer=lambda x: dumps(x).encode("utf-8")
)

# read data
df = pd.read_csv(r"data/2020-Jan_sample.csv")
dict_data = df.to_dict(orient='records')

for i in range(len(dict_data)):
    producer.send(TOPIC_NAME, value=dict_data[i])
    producer.flush()
