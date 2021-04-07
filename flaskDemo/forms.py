from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flaskDemo import db
from flaskDemo.models import User, Game, getGame, getGameFactory
from wtforms.fields.html5 import DateField




class GameUpdateForm(FlaskForm):
#    gameID = IntegerField('Game Number', validators=[DataRequired])
    team1 = IntegerField('Team Number', validators=[DataRequired])

    team2 = IntegerField('Team Number', validators=[DataRequired])

    date = DateField("Date Played", format='%Y-%m-%d')






class GameForm(GameUpdateForm):
    gameID = IntegerField('Game Number', validators=[DataRequired])
    submit = SubmitField('Add this game')

    def validate_gameID(self, gameID):      #gameID is the primary key; must be unique
        game = Game.query.filter_by(gameID=gameID.data).first()
        if game:
            raise ValidationError('This game already exists')

