from fastavro import writer
import io
import uuid
from app.streaming.avroschema import schema


class AvroSerialiser:
    def __init__(self):
        pass

    def serialise_message(self, message):
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': message.get_author(),
                                 'type': message.get_message_type().value,
                                 'raw_text': message.get_raw_message(),
                                 'timestamp': message.get_time_created().timestamp(),
                                 'html': message.get_html()}])
        return buffer.getvalue()
