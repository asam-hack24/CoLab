from app.messages.message import Message


class TextMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message):
        super(TextMessage, self).__init__(author=author, last_author=last_author,
                                          time_created=time_created, time_last_modified=time_last_modified,
                                          message=message)
        self._html_message = None

    def serialize(self):
        pass

    def _do_deserialize(self, message):
        pass

    def _do_create_html_message(self):
        self._html_message = self._message
