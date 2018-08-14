from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from database import DataBase

class webDBManager(object):
	"""
	A class to manage the web portion of the database.

	Variables:
		webDatabase <DataBase>
	
	Methods:
		uploadUser inserts a username and hashed_password to the web table in the engine database
		getUser returns a user object as determined by an unique id
		checkUserName bool to see if a given username is already in the database
		setPassword uses werkzeug.security to hash a password
		checkPassword uses werkzeug.security to compare if a password is the same as the hashed password
		topTenScores returns the ten greatest tile counts in the database
		topTenScoresForPlayer returns the ten greatest tile counts for a given user

	"""
	def __init__(self):

		self.webDatabase = DataBase("engine.db")



	def uploadUser(self, username, password):
		"""
		Inserts a username and hashed_password to the web table in the engine database.
		 Calls setPassword to hash the input password

		Input:
			username <str>
			password <str>

		Output:
			Insert into engine.db
		"""
		if not self.checkUserName(username):
			hashed_password = self.setPassword(password)
			upload_user_string = ("INSERT INTO webInfo VALUES ('{0}', '{1}');").format(username, hashed_password)
			# print(username + hashed_password)

			self.webDatabase.execute(upload_user_string)

		else:
			print("There was a problem uploading {0}, namely it already exists and wasn't caught".format(username))



	def getUser(self, new_user_id):
		"""
		Runs a sqlite check to find the information for a user as determined by the 
		 user id, and creates a User object with the given information.

		Input:
			new_user_id <int>

		Output:
			new_user <User>
		"""
		find_user_string = ("SELECT * FROM webInfo"
							" WHERE rowid='{0}';".format(new_user_id)
							)
		is_user = self.webDatabase.fetch_one_execute(find_user_string)
		if is_user is not None:
			new_user = User(is_user[0])

		else:
			new_user = None

		return new_user



	def checkUserName(self, username):
		"""
		A sqlite check in the database to see if a username is already in the database

		Input:
			username <str>

		Output:
			<bool>
		"""
		command_string_user = ("SELECT 1 FROM webInfo"
							   " WHERE user_name='{0}';".format(username)
							  )
		
		true_user = self.webDatabase.fetch_one_execute(command_string_user)
		if true_user is not None:
			return True

		return False



	def setPassword(self, password):
		"""
		Uses werkzeug.security to turn a string into a hash

		Input:
			password <str>

		Output:
			hashed_password <str>
		"""
		return generate_password_hash(password)



	def checkPassword(self, username, password):
		"""
		Uses sqlite and werkzeug.security to check if the user gave a password
		 equivalent to the password used to register

		Input:
			username <str>
			password <str>

		Output:
			<bool>
		"""
		password_hash_string = ("SELECT password_hash FROM webInfo"
								" WHERE user_name='{0}';").format(username)
		password_hash = self.webDatabase.fetch_one_execute(password_hash_string)
		if password_hash is not None:
			password_hash = self.webDatabase.fetch_one_execute(password_hash_string)[0]
			return check_password_hash(password_hash, password)

		return False



	def topScores(self):
		"""
		Uses sqlite to take ten of the rows by the top tile counts from the game table

		Output:
			top_ten <str>
		"""
		show_scores_string = ("SELECT * FROM gameInfo"
							  " ORDER BY tiles DESC"
							  " ;"
							 )
		top_ten = self.webDatabase.fetch_all_execute(show_scores_string)
		return top_ten


	def topScoresForPlayer(self, username):
		"""
		Uses sqlite to take ten rows from the game table for a given username

		Input:
			username <str>

		Output:
			top_ten <str>
		"""
		show_scores_string = ("SELECT * FROM gameInfo"
							  " WHERE player_name='{0}'"
							  " ORDER BY tiles DESC"
							  " ;".format(username)
							 )
		top_ten = self.webDatabase.fetch_all_execute(show_scores_string)
		if top_ten is not None:
			return top_ten

		else:
			return ("None", "None", "None", 0, 0)








class User(UserMixin):
	"""
	Inherits UserMixin class from Flask. Is used to track current user and login/out functionality through Flask.

	Variables:
		username <str>
		id <int>

	Methods:
		getUserID gives the unique id for the given user
	"""
	def __init__(self, username):
		self.username = username
		super().__init__()
		self.id = self.getUserID()

	def getUserID(self):
		"""
		Uses sqlite to pull the unique id for a given user

		Output:
			user_ID <int>
		"""
		get_rowID_string = ("SELECT rowid FROM webInfo"
							" WHERE user_name='{0}';".format(self.username)
							)
		user_ID = DataBase("engine.db").fetch_one_execute(get_rowID_string)

		if user_ID is not None:
			return user_ID[0]
		else:
			return -1

