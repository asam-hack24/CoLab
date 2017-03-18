from kafka import KafkaProducer
from streaming import avroserialise

producer = KafkaProducer(bootstrap_servers=['192.168.252.82'])
serialiser = avroserialise.AvroSerialise()
for n in range(100):
    buffer = serialiser.serialise(message="message number " + str(n))
    producer.send('test_avro_topic', buffer)
