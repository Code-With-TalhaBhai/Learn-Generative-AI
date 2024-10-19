```
docker network create -d bridge kafka-network

docker network ls

docker run -p 9092:9092 --network kafka-network --name kafka-backend apache/kafka:3.8.0(Then create topics,producer,consumer inside it)


docker run -it -p 8080:8080 --network kafka-network --name kafka-frontend -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui
```