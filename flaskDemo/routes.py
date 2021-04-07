import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskDemo import app, db, bcrypt

# ToDo create forms and models
from flaskDemo.forms import GameForm
from flaskDemo.models import Arena, Coach, Game, Player, Referee, Ref_Game, Team, Trainer

from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():

@app.route("/about")
def about():

# ToDo Confirm pages to be included for the purpose of Lab4c
# @app.route("/register")
# def register():
#
# @app.route("/login")
# def login():
#
# @app.route("/logout")
# def logout():
#
# @app.route("/account")

# For this lab will be updating/deleting on GAME db
@app.route("/game/new", methods=['GET', 'POST'])
def new_game():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(gameID=form.gameID.data, )
    return render_template('create_game.html', title='New Game',
                           )

@app.route("/game/<gameID>")
def game(gameID):

@app.route("/game/<gameID>/update", methods=['GET', 'POST'])
def update_game(gameID):

@app.route("/game/<gameID>/delete", methods=['GET', 'POST'])
def delete_game(gameID):
