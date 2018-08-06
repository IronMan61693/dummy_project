from flask import render_template, redirect, flash, url_for, Blueprint
from flask_login import current_user, login_user, logout_user

from WebForms import LoginForm, RegistrationForm
from WebDBConnect import webDBManager, User

# Blueprint from flask simplifies the WebRun's use of various routes
route_page = Blueprint('route_page', __name__, template_folder='templates')
dataCheck = webDBManager()



# Given the base url sets the extension / or /home to the html code as described WebBase.html
@route_page.route('/')
@route_page.route('/home')
def home_page():
	return render_template("WebBase.html", title='Wacky Fun')



# Given the base url sets the extension /score to the html code as described WebScores.html
@route_page.route('/score')
def score_page():
	ten_scores = dataCheck.topTenScores()
	
	return render_template("WebScores.html", title='Score Page', ten_scores = ten_scores)


# Given the base url sets the extension /login to the html code as described WebLogin.html
@route_page.route('/login', methods=['GET', 'POST'])
def login_page():
	"""
	Checks if the current user is logged in, if it is sends the user to the home page
	 If the user is not logged on creates a LoginForm from WebForms. Uses the form method
	 validate_on_submit to submit the information provided in the form. Checks if the username
	 and associated password are correct to login. Creates a User called user and then uses Flask
	 login extension to login the associated user. Once logged in send to the home page.
	"""
	if current_user.is_authenticated:
		return redirect(url_for('route_page.home_page'))

	form = LoginForm()

	if form.validate_on_submit():

		userCheck = dataCheck.checkUserName(form.username.data)

		if not (userCheck and dataCheck.checkPassword(form.username.data, form.password.data)):

			flash('Invalid username or password')
			return redirect(url_for('route_page.login_page'))

		user = User(form.username.data)
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('route_page.home_page'))

	return render_template("WebLogin.html", title='Sign In', form=form)



# uses Flask-login extension to logout the current user and sends the connection to home page.
@route_page.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('route_page.home_page'))



# Given the base url sets the extension /register to the html code as described WebRegister.html
@route_page.route('/register', methods=['GET', 'POST'])
def register_page():
	"""
	Checks if the current user is logged in and if so sends them to the home page.
	 Creates an instance of the RegistrationForm from WebForms and uses Flask form to
	 submit the filled in information. Then sends the information from the form to 
	 the database to create the user.
	"""
	if current_user.is_authenticated:
		return redirect(url_for('route_page.home_page'))

	form = RegistrationForm()
	if form.validate_on_submit():

		dataCheck.uploadUser(form.username.data, form.password.data)
		flash('Yay, you are now a registered member')
		return redirect(url_for('route_page.login_page'))

	return render_template('WebRegister.html', title = 'Register', form=form)


# Given the base url sets the extension /characters to the html code as described WebCharacter.html
@route_page.route('/characters')
def characters_page():
	if current_user.is_authenticated:
		char_scores = dataCheck.topTenScoresForPlayer(current_user.username)
		return render_template("WebCharacter.html", title='Character Page', char_scores = char_scores)

	else:
		return redirect(url_for('route_page.login_page'))

