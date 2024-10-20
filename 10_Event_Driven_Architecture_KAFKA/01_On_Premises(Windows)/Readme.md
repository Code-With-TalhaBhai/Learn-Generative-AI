# Installation

First step is to download `binary file` of Apache Kafk at [Kafka Download](https://kafka.apache.org/downloads)


# Setup Kafka Environment

NOTE: Your local environment must have Java 8+ installed.

Kafka can either be used with `KRaft` or `zookeeper`, but for windows we used `zookeeper`. If you are using UNIX environment(Linux or MAC) see the documentation [Kafka Quickstart](https://kafka.apache.org/quickstart)


## Kafka with zookeeper

1. First start the zookeeper service:
    ```bash
    bin/windows/zookeeper-server-start.bat config/zookeeper.properties
    ```


2. Start the Kafka broker service:
    ```bash
    bin/windows/kafka-server-start.bat config/server.properties
    ```


3. Create Topic To Store Your Events:
    ```bash
    bin/windows/kafka-topics.bat --create --topic quickstart-events --bootstrap-server localhost:9092
    ```


4. Write some events into the Topic:
    ```bash
    bin/windows/kafka-console-producer.bat --topic quickstart-events --bootstrap-server localhost:9092
    

    $ This is my first event
    $ This is my second event 
    ```


5. Read the Events:
    ```bash
    bin/windows/kafka-console-consumer.bat --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
    ```