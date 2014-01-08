__author__ = 'zifnab'

from datetime import datetime

from mongoengine import Document
from mongoengine import StringField, DateTimeField, ReferenceField
from flask_login import UserMixin

from util import random_string


class User(Document, UserMixin, object):
    username = StringField(required=True, unique=True, max_length=16, min_length=3)
    hash = StringField(required=True)
    email = StringField(required=False)
    registration_date = DateTimeField(default=datetime.now)


    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_active(self):
        return True
    def get_id(self):
        return self.username

    meta = {
        'index': ['username'],
        'collection': 'users'
    }



class Paste(Document):
    name = StringField(required=True, default=random_string())
    paste = StringField(required=True)
    time = DateTimeField(required=True, default=datetime.utcnow)
    expire = DateTimeField(required=False)
    user = ReferenceField(User, required=False)


