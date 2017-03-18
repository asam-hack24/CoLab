from app.messages.message import (Message, MessageType)


class RMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message, html=None):
        super(RMessage, self).__init__(author=author, last_author=last_author,
                                       time_created=time_created, time_last_modified=time_last_modified,
                                       message=message, html=html)
        self._message_type = MessageType.R

    def serialize(self):
        return self._serializer.serialise_message(self)

    def _do_create_html_message(self):
        raise RuntimeError()
