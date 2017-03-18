from kafka import KafkaProducer
from app.streaming.avroserialiser import AvroSerialiser

producer = KafkaProducer(bootstrap_servers=['192.168.252.82'])
serialiser = AvroSerialiser()
for n in range(100):
    buffer = serialiser.serialise(raw_text="message number " + str(n))
    producer.send('test_avro_topic', buffer)
