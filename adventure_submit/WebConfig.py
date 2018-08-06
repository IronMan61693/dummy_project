import os


class Config(object):
	"""
	Configuration modifications for Flask object.
	"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_sneaky_secret_key yo'

