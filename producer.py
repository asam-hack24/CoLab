from kafka import KafkaProducer
from streaming import avroserialise

producer = KafkaProducer(bootstrap_servers=['localhost'])
serialiser = avroserialise.AvroSerialise()
for n in range(100):
    buffer = serialiser.serialise(message="message number " + str(n))
    producer.send('test_avro_topic', buffer)
