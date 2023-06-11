from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# Kafka setting
TOPIC_NAME = "test1"
BOOTSTRAP_SERVERS = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: loads(x.decode("utf-8"))
)

event_types = ['view', 'cart', 'remove_from_cart', 'purchase']

price_ranges = {
    "0-10": {event_type: 0 for event_type in event_types},
    "10-20": {event_type: 0 for event_type in event_types},
    "20-30": {event_type: 0 for event_type in event_types},
    "30-40": {event_type: 0 for event_type in event_types},
    "40-50": {event_type: 0 for event_type in event_types},
    ">50": {event_type: 0 for event_type in event_types}
}

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
fig.tight_layout(pad=3.5)

titles = ["View", "Cart", "Remove from Cart", "Purchase"]
x_label = "Price Range"
y_label = "Transaction Count"

# 繪製四個子圖並初始化直方圖柱狀體
bars = []
for i, ax in enumerate(axes.flatten()):
    ax.set_title(titles[i])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    bar = ax.bar(price_ranges.keys(), [0] * len(price_ranges), tick_label=list(price_ranges.keys()))
    bars.append(bar)

def update_graph():
    # 更新直方圖柱狀體的高度
    for j, bar in enumerate(bars):
        for k, rect in enumerate(bar):
            price_range = list(price_ranges.keys())[k]
            rect.set_height(price_ranges[price_range][event_types[j]])

    max_count = max([price_ranges[key][event_type] for key in price_ranges for event_type in event_types])
    for ax in axes.flatten():
        ax.set_ylim(0, max_count + 1)

    plt.draw()

# read data from topic
for msg in consumer:
    event_type = msg.value["event_type"]
    price = msg.value["price"]

    # 根據不同價格範圍和事件類型更新交易數量
    if 0 <= price < 10:
        price_ranges["0-10"][event_type] += 1
    elif 10 <= price < 20:
        price_ranges["10-20"][event_type] += 1
    elif 20 <= price < 30:
        price_ranges["20-30"][event_type] += 1
    elif 30 <= price < 40:
        price_ranges["30-40"][event_type] += 1
    elif 40 <= price < 50:
        price_ranges["40-50"][event_type] += 1
    elif price > 50:
        price_ranges[">50"][event_type] += 1

    update_graph()
    plt.pause(0.01)
