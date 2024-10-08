1. First step is to pull the image [Apache Kafka](https://hub.docker.com/layers/apache/kafka/3.8.0/images/sha256-c9aea96a4813e77e703541b1d8f7d58c9ee05b77353da33684db55c840548791?context=explore)

```
    docker pull apache/kafka:3.8.0
```

2. Then just create the container using this image
```
    docker run -p 9092:9092 apache/kafka:3.8.0
```

3. Then check container name or id
```
    docker ps
```

4. Then, enter into the container using interactive mode.
```
    docker exec -it [container_name or id] /bin/bash
```

The working directory which has all shell scripts of kafka is:
```
/opt/kafka/bin/
```

5. Then, create `topic` for the event using the command: 
```
    /opt/kafka/bin/kafka-topics.sh --create --topic first-docker-topic --bootstrap-server localhost:9092
```


6. Then, create the `producer` of the event using: 
```
    /opt/kafka/bin/kafka-console-producer.sh --topic first-docker-topic --bootstrap-server localhost:9092
```
send some events from here.


7. Open, new terminal and again step into the container again defined at step 4
```
    /opt/kafka/bin/kafka-console-consumer.sh --topic first-docker-topic --from-beginning --bootsrap-server localhost:9092
```

Observe the events.