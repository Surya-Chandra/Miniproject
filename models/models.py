from config.config import db
import datetime


class User(db.Document):
    name = db.StringField(required=True, max_length=20)
    email = db.StringField(required=True)


class Roles(db.Document):
    name = db.StringField(required=True, unique=True, max_length=20)
    permissions = db.ListField(db.StringField())


class Group(db.Document):
    name = db.StringField(required=True, max_length=30)
    visibility = db.StringField(default='public')
    role_dict = db.DictField()  # fill with {'user_id':'role'}
    date_created = db.DateTimeField(default=datetime.datetime.now())
    last_active_dict = db.DictField()  # fill with {'user_id':'last active time'}


class Post(db.Document):
    user_id = db.ReferenceField('User')
    group_id = db.ReferenceField('Group')
    content = db.StringField(required=True, max_length=200)
    # approval is set to true for now
    approval = db.StringField(Default=True, max_length=10)
    date_created = db.DateTimeField(default=datetime.datetime.now())


class Comment(db.Document):
    user_id = db.ReferenceField('User')
    post_id = db.ReferenceField('Post')
    content = db.StringField(required=True, max_length=75)
    date_created = db.DateTimeField(default=datetime.datetime.now())




