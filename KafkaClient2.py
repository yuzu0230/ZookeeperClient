from kafka.admin import KafkaAdminClient, NewTopic


if __name__ == "__main__":
    admin_client = KafkaAdminClient(
        bootstrap_servers=["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"], 
    )
    topic_list = []
    for topic in ["test1", "test2"]:
        topic_list.append(NewTopic(name=topic, num_partitions=3, replication_factor=1))
    
    admin_client.create_topics(new_topics=topic_list, validate_only=False)