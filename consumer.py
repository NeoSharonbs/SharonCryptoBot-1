from kafka import KafkaConsumer
import psycopg2
import json

consumer = KafkaConsumer(
    'crypto_prices',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect(
    dbname='mydb',
    user='user',
    password='password',
    host='postgres'
)
cursor = conn.cursor()

for message in consumer:
    data = message.value
    cursor.execute(
        "INSERT INTO prices (currency, price) VALUES (%s, %s)",
        ('bitcoin', data['bitcoin']['usd'])
    )
    conn.commit()