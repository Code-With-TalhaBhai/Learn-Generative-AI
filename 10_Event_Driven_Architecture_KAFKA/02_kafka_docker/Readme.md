
docker run -p 9092:9092 apache/kafka:3.8.0


docker exec -it 8c7437c479ff /bin/bash

cd /opt/kafka/bin/

/opt/kafka/bin/kafka-topics.sh --create --topic first-docker-topic --bootstrap-server localhost:9092

/opt/kafka/bin/kafka-console-producer.sh --topic first-docker-topic --bootstrap-server localhost:9092


/opt/kafka/bin/kafka-console-consumer.sh --topic first-docker-topic --from-beginning --bootsrap-server localhost:9092