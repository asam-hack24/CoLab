from app import app
from flask import Flask, session, redirect, url_for, escape, request, Response, render_template
from kafka import KafkaConsumer
from app.streaming.avrodeserialiser import AvroDeserialiser
from time import sleep


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


consumer = KafkaConsumer('test_avro_topic',
                         group_id=None,
                         bootstrap_servers=['192.168.252.82'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False)

all_messages = ['A', 'B', 'C']
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
                        yield "data: %s\n\n" % message.get_html()

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('/send', methods=['POST'])
def send():
    print(request.form['message'])
    all_messages.append(request.form['message'])
    return ""
