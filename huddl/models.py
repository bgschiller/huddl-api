import logging
import json

logger = logging.getLogger(__name__)
logger.debug('top of models')

from uuid import uuid4
from flask import url_for
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from huddl import app, db, login_manager

def uuid_hex():
    return uuid4().hex

class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True, default=uuid_hex)
    name = db.Column(db.String(255))
    fb_id = db.Column(db.String(31), unique=True)
    fb_access_token = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(31))
    create_date = db.Column(db.DateTime, default=db.func.now())

    def get_id(self):
        return unicode(self.id)
    def is_active(self):
        return True
    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

memberships = db.Table('memberships',
    db.Column('user_id', db.String(32), db.ForeignKey('user.id')),
    db.Column('group_id', db.String(32), db.ForeignKey('group.id')))

class Group(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=uuid_hex)
    name = db.Column(db.String(255))
    members = db.relationship('User', secondary=memberships,
        backref=db.backref('groups'))
    events = db.relationship('Event', backref='group')

class Event(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=uuid_hex)
    name = db.Column(db.String(255))
    group_id = db.Column(db.String(32), db.ForeignKey('Group')
