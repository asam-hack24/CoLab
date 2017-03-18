from app.messages.message import (Message, MessageType)
import base64
import os


class ImageMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message):
        message_blob = ImageMessage._convert_to_blob(message)
        super(ImageMessage, self).__init__(author=author, last_author=last_author,
                                           time_created=time_created, time_last_modified=time_last_modified,
                                           message=message_blob)
        self._message_type = MessageType.IMAGE

    def serialize(self):
        return self._serializer.serialise(raw_text=self._message)

    def _do_create_html_message(self):
        self._html_message = self._message

    @staticmethod
    def _convert_to_blob(full_file_path):
        if not os.path.exists(full_file_path):
            raise RuntimeError("The file path {} does not seem to exist".format(full_file_path))

        with open(full_file_path, "rb") as image_file:
            message = base64.b64encode(image_file.read())

        if message is None:
            raise RuntimeError("The image could not be converted into a blob")
        return message
