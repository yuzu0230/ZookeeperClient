from kafka import KafkaConsumer
from json import loads
from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

# kafka settings
TOPIC_NAME = "test1"
BOOTSTRAP_SERVERS = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]

# max size in x-axis
LIMIT = 20

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: loads(x.decode("utf-8")) 
    )

fig, ax = plt.subplots(figsize=(12, 5))
event_time = []
prices = []

line, = ax.plot_date(event_time, prices, "-")
ax.set_xlabel("event_time")
ax.set_ylabel("price")
ax.set_title("Real-time data")


date_format = DateFormatter("%Y-%m-%d %H:%M:%S")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()  

def update_graph():
    line.set_data(event_time, prices)
    ax.relim()
    ax.set_xlim(event_time[0], event_time[-1])
    ax.set_ylim(0, max(prices))
    plt.draw()

# read data from topic
for msg in consumer:
    datetime_str = msg.value["event_time"][:19]
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    event_time.append(dt)
    prices.append(msg.value["price"])

    if len(event_time) >= LIMIT:
        event_time = event_time[-LIMIT:]
        prices = prices[-LIMIT:]
        

    update_graph()
    plt.pause(0.03)
 