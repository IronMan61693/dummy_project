#!/usr/bin/env python3

from flask import Flask
from flask_login import LoginManager


from WebConfig import Config
from WebRoutes import route_page
from WebDBConnect import webDBManager



webApp = Flask(__name__)

webApp.config.from_object(Config)
webApp.register_blueprint(route_page)
webDatabase = webDBManager()
login = LoginManager(webApp)
login.login_view = 'login_page'


@login.user_loader
def load_user(user_id):
	return webDatabase.getUser(user_id)




webApp.run(debug=True)


# @login_manager.user_loader
# def load_user(username):
# 	get_rowID_string = ("SELECT rowid FROM webInfo"
# 						" WHERE user_name='{0}';".format(username)
# 						)
# 	user_ID = DataBase("engine.db").fetch_one_execute(get_rowID_string)

# 	if user_ID is not None:
# 		return user_ID[0]
# 	else:
# 		return -1
# if __name__ == "__main__":
# 	webApp.run(debug=True)



