from app import app
from flask import Flask, session, redirect, url_for, escape, request, Response, render_template
from kafka import KafkaConsumer
from kafka import KafkaProducer
from app.streaming.avroserialiser import AvroSerialiser
from app.streaming.avrodeserialiser import AvroDeserialiser
from time import sleep


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


KAFKA_BROKER = '192.168.252.82'
consumer = KafkaConsumer('test_avro_topic',
                         group_id=None,
                         bootstrap_servers=[KAFKA_BROKER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False)
producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
serialiser = AvroSerialiser()
all_messages = []
deserialiser = AvroDeserialiser()


@app.route('/get_messages')
def get_messages():
    if request.headers.get('accept') == 'text/event-stream':
        def script():
            sleep(0.1)  # this fixes missing messages, don't remove
            partitions = consumer.poll(timeout_ms=100, max_records=5)
            if len(partitions) > 0:
                for p in partitions:
                    for response in partitions[p]:
                        message = deserialiser.deserialise(response.value)
                        all_messages.append(message)
                        yield "data: %s\n\n" % message.get_html()

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('/send', methods=['POST'])
def send():
    print(request.form['message'])
    buffer = serialiser.serialise(raw_text=request.form['message'])
    producer.send('test_avro_topic', buffer)
    return ""
