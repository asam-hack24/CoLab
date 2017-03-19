from app.messages.message import (Message, MessageType)
from app.script_execution.r_executor import RExecutor
import re


class RMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified, message, topic, html=None):
        super(RMessage, self).__init__(author=author, last_author=last_author,
                                       time_created=time_created, time_last_modified=time_last_modified,
                                       message=message, topic=topic, html=html)
        self._message_type = MessageType.R

    def serialize(self):
        return self._serializer.serialise_message(self)

    def _do_create_html_message(self):
        executor = RExecutor()
        raw_message = self.get_raw_message()
        self._html_message = executor.execute(raw_message)
        self._html_message = re.sub(r'\>\n', '>', self._html_message)
        self._html_message = re.sub(r'\n\<', '<', self._html_message)
        self._html_message = self._html_message.replace('\n', '<br>')
