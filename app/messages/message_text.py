from app.messages.message import (Message, MessageType)


class TextMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, topic, message):
        super(TextMessage, self).__init__(author=author, last_author=last_author,
                                          time_created=time_created, time_last_modified=time_last_modified,
                                          topic=topic, message=message)
        self._message_type = MessageType.TEXT

    def serialize(self):
        return self._serializer.serialise_message(self)

    def _do_create_html_message(self):
        self._html_message = self._message
