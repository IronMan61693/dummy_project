from flask import render_template, redirect, flash, url_for, Blueprint
from flask_login import current_user, login_user, logout_user

# from WebRun import *
from WebForms import LoginForm, RegistrationForm
from WebDBConnect import webDBManager, User

route_page = Blueprint('route_page', __name__, template_folder='templates')
dataCheck = webDBManager()

@route_page.route('/')
@route_page.route('/home')
def home_page():
	return render_template("WebBase.html", title='Wacky Fun')


@route_page.route('/score')
def score_page():
	ten_scores = dataCheck.topTenScores()
	return render_template("WebScores.html", title='Score Page', ten_scores = ten_scores)

@route_page.route('/login', methods=['GET', 'POST'])
def login_page():
	if current_user.is_authenticated:
		return redirect(url_for('route_page.home_page'))

	form = LoginForm()

	if form.validate_on_submit():

		userCheck = dataCheck.checkUserName(form.username.data)

		# Change back to one line when done trouble shooting

		if not userCheck :

			flash('Invalid username')
			return redirect(url_for('route_page.login_page'))

		if not dataCheck.checkPassword(form.username.data, form.password.data):
			flash('Invalid password')
			return redirect(url_for('route_page.login_page'))

		user = User(form.username.data)
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('route_page.home_page'))

	return render_template("WebLogin.html", title='Sign In', form=form)

@route_page.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('route_page.home_page'))

@route_page.route('/register', methods=['GET', 'POST'])
def register_page():
	if current_user.is_authenticated:
		return redirect(url_for('route_page.home_page'))

	form = RegistrationForm()
	if form.validate_on_submit():

		dataCheck.uploadUser(form.username.data, form.password.data)
		flash('Yay, you are now a registered member')
		return redirect(url_for('route_page.login_page'))

	return render_template('WebRegister.html', title = 'Register', form=form)

@route_page.route('/characters')
def characters_page():
	if current_user.is_authenticated:
		char_scores = dataCheck.topTenScoresForPlayer(current_user.username)
		return render_template("WebCharacter.html", title='Character Page', char_scores = char_scores)

	else:
		return redirect(url_for('route_page.login_page'))

