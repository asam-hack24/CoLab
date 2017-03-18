from abc import ABCMeta, abstractmethod
from datetime import datetime
from app.streaming.avroserialise import AvroSerialise
from enum import Enum


class MessageType(Enum):
    TEXT = 1
    PYTHON = 2
    R = 3


class Author:
    def __init__(self, first_name, last_name, author_id):
        self._first_name = first_name
        self._last_name = last_name
        self._author_id = author_id


class Message(metaclass=ABCMeta):
    def __init__(self, author, last_author, time_created, time_last_modified, message):
        if not isinstance(time_created, datetime):
            raise ValueError("time_stamp: Expected a datetime object, got {}".format(type(time_created)))
        if not isinstance(time_last_modified, datetime):
            raise ValueError("last_modified: Expected a datetime object, got {}".format(type(time_last_modified)))
        if not isinstance(author, Author):
            raise ValueError("author: Expected an Author object, got {}".format(type(author)))
        if not isinstance(last_author, Author):
            raise ValueError("last_author: Expected an Author object, got {}".format(type(last_author)))

        self._author = author
        self._last_author = last_author
        self._time_created = time_created
        self._time_last_modified = time_last_modified
        self._message = message
        self._html_message = None
        self._message_type = None
        self._serializer = AvroSerialise()

    @abstractmethod
    def serialize(self):
        pass

    def get_html(self):
        if self._html_message is None:
            self._do_create_html_message()
        return self._html_message

    @abstractmethod
    def _do_create_html_message(self):
        pass

    def get_time_created(self):
        return self._time_created

    def get_time_last_modified(self):
        return self._time_last_modified

    def get_author(self):
        return self._author

    def get_last_author(self):
        return self._last_author

    def get_message_type(self):
        return self.message_type
