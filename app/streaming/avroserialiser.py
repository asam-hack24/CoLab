from fastavro import writer
import io
import uuid
from datetime import datetime
from app.streaming.avroschema import schema


class AvroSerialiser:
    def __init__(self):
        pass

    def serialise_message(self, message):
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': message.get_author(),
                                 'type': message.get_message_type(),
                                 'raw_text': message.get_raw_message(),
                                 'timestamp': datetime.now().timestamp(),
                                 'html': message.get_html()}])
        return buffer.getvalue()

    def serialise(self, raw_text='', message_type=1, author='Bob'):
        """Generate a unique id for the message and serialise it"""
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': author,
                                 'type': message_type,
                                 'raw_text': raw_text,
                                 'timestamp': datetime.now().timestamp(),
                                 'html': raw_text}])
        return buffer.getvalue()
