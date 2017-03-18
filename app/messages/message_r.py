from app.messages.message import Message


class RMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message):
        super(RMessage, self).__init__(author=author, last_author=last_author,
                                       time_created=time_created, time_last_modified=time_last_modified,
                                       message=message)

    def serialize(self):
        pass

    def _do_deserialize(self, message):
        pass

    def _do_create_html_message(self):
        raise RuntimeError()