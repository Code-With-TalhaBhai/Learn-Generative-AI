from fastapi import FastAPI,Depends
from contextlib import asynccontextmanager
from aiokafka import AIOKafkaConsumer,AIOKafkaProducer
import asyncio
from typing import Annotated,AsyncGenerator
from confluent_kafka.admin import AdminClient, NewTopic
import time


TOPIC = "my_fastapi_topic"
# broker_url = "http://host.docker.internal:19092"
broker_url = "broker:19092"

async def create_topic():
    RETRY_DELAY = 7
    MAX_RETRIES = 5
    print('before attempt')
    for attempt in range(0,MAX_RETRIES):
        print('before try')
        try:
            admin_client = AdminClient({'bootstrap.servers': broker_url})
            topic = NewTopic(TOPIC,num_partitions=1,replication_factor=1)
            admin_client.create_topics([topic])
            return admin_client
        except Exception as e:
            print(f"Attempting to connect kafka {attempt} times")
            await asyncio.sleep(RETRY_DELAY)
    raise ConnectionError("Could not connect to Kafka even after {MAX_RETRIES} time")


async def consume_messages(topic,bootstrap_server):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_server,
        group_id="my_group"
    )
    await consumer.start()

    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()


async def create_producer():
    producer = AIOKafkaProducer(bootstrap_servers=broker_url)
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()


@asynccontextmanager
async def lifespan(app:FastAPI):
    print('lifespan start')
    await create_topic()
    task = asyncio.create_task(consume_messages(TOPIC,broker_url))
    yield
    await task



app = FastAPI(lifespan=lifespan)


@app.get('/')
def index():
    return {"Hello":"World"}


@app.post('/create-producer')
async def create_producer(message:str,create_producer:Annotated[AIOKafkaProducer,Depends(create_producer)]):
    async for producer in create_producer(): #Async Generator
        await producer.send_and_wait(TOPIC,message.encode('utf-8'))

    return {'msg':message}
