from fastavro import reader, writer
import io
import uuid


class AvroSerialise:
    schema = {
        'name': 'Message',
        'type': 'record',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'author', 'type': 'string'},
            {'name': 'type', 'type': 'string'},
            {'name': 'text', 'type': 'string'},
            {'name': 'html', 'type': 'string'},
        ],
    }

    def __init__(self):
        pass

    def serialise(self, message=''):
        """Generate a unique id for the message and serialise it"""
        buffer = io.BytesIO()
        writer(buffer, self.schema, [{'id': uuid.uuid4().int,
                                      'author': 'Bob',
                                      'type': 'text',
                                      'text': message,
                                      'html': message}])
        return buffer.getvalue()

    def deserialise(self, buffer):
        output = reader(io.BytesIO(buffer), self.schema)
        return output
