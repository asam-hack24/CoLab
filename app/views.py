from app import app
from flask import redirect, url_for, request, Response, render_template, make_response
from kafka import KafkaConsumer
from kafka import KafkaProducer
from app.streaming.avroserialiser import AvroSerialiser
from app.streaming.avrodeserialiser import AvroDeserialiser
from time import sleep
from app.messages.message import MessageType
from app.messages.message_text import TextMessage
from app.messages.message_python import PythonMessage
from app.messages.message_r import RMessage
from app.messages.message_image import (ImageMessage, get_blob_from_file)
from app.script_execution.script_creator import (save_python_notebook_to_file, save_r_notebook_to_file)
from datetime import datetime
import configparser
import os
import json
import io


@app.route('/')
@app.route('/index')
def index():
    return render_template("UI_flask.html")


@app.route('/ui')
def ui():
    return render_template("UI_flask.html")


config = configparser.ConfigParser()
config.read(os.path.join('app', 'userconfig.ini'))
USERNAME = config['user']['name']
KAFKA_BROKER = '192.168.252.82'
consumer = KafkaConsumer('test_avro_topic',
                         group_id=None,
                         bootstrap_servers=[KAFKA_BROKER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False)
events_consumer = KafkaConsumer('events',
                                group_id=None,
                                bootstrap_servers=[KAFKA_BROKER],
                                auto_offset_reset='earliest',
                                enable_auto_commit=False)
producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
serialiser = AvroSerialiser()
all_messages = []
deserialiser = AvroDeserialiser()


@app.route('/get_events')
def get_events():
    if request.headers.get('accept') == 'text/event-stream':
        def script():
            sleep(0.1)  # this fixes missing messages, don't remove
            partitions = events_consumer.poll(timeout_ms=100, max_records=50)
            if len(partitions) > 0:
                for p in partitions:
                    for response in partitions[p]:
                        event_type, name = deserialiser.deserialise_event_message(response.value)
                        payload = {'event_type': event_type, 'name': name}
                        yield "data: %s\n\n" % json.dumps(payload)

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('/get_messages')
def get_messages():
    if request.headers.get('accept') == 'text/event-stream':
        def script():
            sleep(0.1)  # this fixes missing messages, don't remove
            partitions = consumer.poll(timeout_ms=100, max_records=50)
            if len(partitions) > 0:
                for p in partitions:
                    for response in partitions[p]:
                        message = deserialiser.deserialise(response.value)
                        all_messages.append(message)
                        raw_message = message.get_raw_message()
                        if isinstance(raw_message, bytes):
                            raw_message = raw_message.decode('utf8')
                        payload = {'message': message.get_html(),
                                   'author': message.get_author(),
                                   'raw_message': raw_message,
                                   'time_created': message.get_time_created().strftime("%H:%M:%S %B %d, %Y"),
                                   'topic': message.get_topic(),
                                   'message_type': message.get_message_type().value}

                        yield "data: %s\n\n" % json.dumps(payload)

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('/send', methods=['POST'])
def send():
    if request.form['type'] == 'text':
        new_message = TextMessage(USERNAME, 'Bob', datetime.now(), datetime.now(), request.form['topic'],
                                  request.form['message'])
    elif request.form['type'] == 'python':
        new_message = PythonMessage(USERNAME, 'Bob', datetime.now(), datetime.now(),
                                    request.form['message'], request.form['topic'])
    elif request.form['type'] == 'r':
        new_message = RMessage(USERNAME, 'Bob', datetime.now(), datetime.now(),
                               request.form['message'], request.form['topic'])
    else:
        raise ValueError('Unrecognised message type in views.py send()')
    buffer = new_message.serialize()
    producer.send('test_avro_topic', buffer)
    return ""


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return ""

        file = request.files['file']
        # if user does not select file, browser also
        # submit  empty part without filename
        if file.filename == '':
            print('No selected file')
            return ''
        # Write the buffer
        encoded = get_blob_from_file(file)
        new_message = ImageMessage(USERNAME, 'Bob', datetime.now(), datetime.now(), request.form['topic'], encoded)
        buffer = new_message.serialize()
        producer.send('test_avro_topic', buffer)
        convert_to_python_notebook()
    return ""

    
@app.route('/create_topic', methods=['POST'])
def create_topic():
    buffer = serialiser.serialise_event_message('create_topic', request.form['topic'])
    producer.send('events', buffer)
    return ""


# This route will prompt a file download with the csv lines
@app.route('/download_python_notebook')
def download():
    file_object = convert_to_python_notebook()
    response = make_response(file_object)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=my_python_notebook.ipynb"
    return response


def convert_to_python_notebook():
    global all_messages
    to_convert = []

    for message in all_messages:
        if message.get_message_type() is not MessageType.R:
            to_convert.append(message)
    file_object = io.BytesIO()
    save_python_notebook_to_file(to_convert, file_object)
    return file_object

# def convert_to_r_notebook():
#     global all_messages
#     to_convert = []
#
#     for message in all_messages:
#         if message.get_message_type() is not MessageType.PYTHON:
#             to_convert.append(message)
#     full_file_path = "/home/anton/sources/hack24/out_r.ipynb"
#     save_r_notebook_to_file(to_convert, full_file_path)
