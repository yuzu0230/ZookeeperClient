from kafka import KafkaProducer
from json import dumps
import pandas as pd


producer = KafkaProducer(bootstrap_servers=["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"],
                         value_serializer=lambda x: dumps(x).encode("utf-8")
)

# producer.send("test1", value={"hello": "world"})
# producer.flush()

df = pd.read_csv(r"data/2020-Jan_sample.csv")
dict_data = df.to_dict(orient='records')
for i in range(len(dict_data)):
    producer.send("test1", value=dict_data[i])
    producer.flush()
