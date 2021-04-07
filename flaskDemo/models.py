from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)





# Create classes for project db tables
class Arena(db.Model):
    __table__ = db.Model.metadata.tables['arena']

class Coach(db.Model):
    __table__ = db.Model.metadata.tables['coach']

class Game(db.Model):
    __table__ = db.Model.metadata.tables['game']

class Player(db.Model):
    __table__ = db.Model.metadata.tables['player']

class Referee(db.Model):
    __table__ = db.Model.metadata.tables['referee']

class Ref_Game(db.Model):
    __table__ = db.Model.metadata.tables['ref_game']

class Team(db.Model):
    __table__ = db.Model.metadata.tables['team']

class Trainer(db.Model):
    __table__ = db.Model.metadata.tables['trainer']
