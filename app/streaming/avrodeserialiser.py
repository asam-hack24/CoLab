from app.streaming.avroschema import schema
from fastavro import reader
import io
from app.messages.message import MessageType
from app.messages.message_text import TextMessage
from datetime import datetime


class AvroDeserialiser:
    def __init__(self):
        pass

    def deserialise(self, buffer):
        output = reader(io.BytesIO(buffer), schema)
        new_message = None
        for message in output:
            if MessageType(message['type']) is MessageType.TEXT:
                new_message = TextMessage(message['author'], 'last_author',
                                          datetime.fromtimestamp(message['timestamp']),
                                          datetime.fromtimestamp(0),
                                          message['raw_text'])
            else:
                raise ValueError('Unrecognised message type in AvroSerialise.deserialise')
        return new_message
