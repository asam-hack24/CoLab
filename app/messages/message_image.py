from app.messages.message import (Message, MessageType)
import io
import base64


def get_blob_from_file(file_handle):
    buffer = io.BytesIO()
    file_handle.save(dst=buffer)
    encoded = base64.b64encode(buffer.getvalue())
    buffer.close()
    return encoded


class ImageMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message, html=None):
        if not isinstance(message, bytes):
            raise RuntimeError("The message has to be bytes")
        super(ImageMessage, self).__init__(author=author, last_author=last_author,
                                           time_created=time_created, time_last_modified=time_last_modified,
                                           message=message, html=html)
        self._message_type = MessageType.IMAGE

    def serialize(self):
        return self._serializer.serialize_binary_message(message=self)

    def _do_create_html_message(self):
        image_as_string = self._message.decode('utf8')
        image_html = '<img src = "data:image/png;base64,{}" / >'.format(image_as_string)
        self._html_message = image_html
