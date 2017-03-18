from fastavro import reader, writer
import io
import uuid
from datetime import datetime
from app.messages.message import MessageType
from app.messages.message_text import TextMessage


class AvroSerialise:
    schema = {
        'name': 'Message',
        'type': 'record',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'author', 'type': 'string'},
            {'name': 'type', 'type': 'string'},
            {'name': 'raw_text', 'type': 'string'},
            {'name': 'html', 'type': 'string'},
            {'name': 'timestamp', 'type': 'int'}
        ],
    }

    def __init__(self):
        pass

    def serialise(self, raw_text=''):
        """Generate a unique id for the message and serialise it"""
        buffer = io.BytesIO()
        writer(buffer, self.schema, [{'id': uuid.uuid4().int,
                                      'author': 'Bob',
                                      'type': 'text',
                                      'raw_text': raw_text,
                                      'timestamp': datetime.now().timestamp(),
                                      'html': raw_text}])
        return buffer.getvalue()

    def deserialise(self, buffer):
        output = reader(io.BytesIO(buffer), self.schema)
        new_message = None
        for message in output:
            if message['type'] == MessageType.TEXT:
                new_message = TextMessage(message['author'], 'last_author',
                                          datetime.fromtimestamp(message['timestamp']),
                                          datetime.fromtimestamp(0),
                                          message['raw_text'])
            else:
                raise ValueError('Unrecognised message type in AvroSerialise.deserialise')
        return new_message
