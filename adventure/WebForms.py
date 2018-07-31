from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, ValidationError, Email, EqualTo

from WebDBConnect import webDBManager


class LoginForm(Form):
	username = TextField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class RegistrationForm(Form):
	

	username = TextField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	password2 = PasswordField(
			'Repeat Password', validators=[Required(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		dataRegCheck = webDBManager()
		
		if dataRegCheck.checkUserName(username):
			raise ValidationError('That username is taken.')

