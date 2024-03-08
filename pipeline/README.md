Firstly, run the following command to initialize accounts and roles for Elasticsearch

```
docker-compose up setup
```

Then run the following command to build containers

```
docker-compose up -d
```

Command to create a Kafka topic (Or go to localhost:9000 to use Kafdrop), here the default topic is 'book'

```
docker-compose exec kafka kafka-topics.sh --create --topic book --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
```

How to connect and send message to Kafka

```
from pipeline import pipeline, topic
kafka_connector = pipeline.KafkaConnector()
kafka_connector.send(msg=) # msg is dict type
```

To check data in Elasticsearch, go to localhost:5601 with username 'elastic', password 'changeme'<br>
Go to Overview in Elastic on sidebar

[![image.png](https://i.postimg.cc/QMkjnWzy/image.png)](https://postimg.cc/NyFhKLB6)

Then go to Indices, scroll down to see the available indexes
