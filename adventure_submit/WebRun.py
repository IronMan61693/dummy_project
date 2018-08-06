#!/usr/bin/env python3

from flask import Flask
from flask_login import LoginManager


from WebConfig import Config
from WebRoutes import route_page
from WebDBConnect import webDBManager


# Creates a Flask object to interface html and python to make a webapplication
webApp = Flask(__name__)

# Sets a security key
webApp.config.from_object(Config)

# Sets web routes
webApp.register_blueprint(route_page)

# An instance of the database manager for user login
webDatabase = webDBManager()

# Uses Flasks login manager
login = LoginManager(webApp)
login.login_view = 'login_page'


@login.user_loader
def load_user(user_id):
	return webDatabase.getUser(user_id)



# Starts loop for web app
webApp.run()


