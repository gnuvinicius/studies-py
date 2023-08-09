import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Order:

    def __init__(self, number, title, value):
        self.id = str(uuid.uuid4())
        self.number = number
        self.title = title
        self.value = value
        self.created_at = datetime.now()

    def __iter__(self):
        return self

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) == 0:
            raise ValueError('title not be empty')
        self.__title = title
