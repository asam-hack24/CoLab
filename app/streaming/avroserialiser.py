from fastavro import writer
import io
import uuid
from datetime import datetime
from app.streaming.avroschema import schema


class AvroSerialiser:
    def __init__(self):
        pass

    def serialise(self, raw_text=''):
        """Generate a unique id for the message and serialise it"""
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': 'Bob',
                                 'type': 1,
                                 'raw_text': raw_text,
                                 'timestamp': datetime.now().timestamp(),
                                 'html': raw_text}])
        return buffer.getvalue()
