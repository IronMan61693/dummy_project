from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# from WebRun import login
from database import DataBase

class webDBManager(object):
	def __init__(self):

		self.webDatabase = DataBase("engine.db")



	def uploadUser(self, username, password):
		if not self.checkUserName(username):
			hashed_password = self.setPassword(password)
			upload_user_string = ("INSERT INTO webInfo VALUES ('{0}', '{1}');").format(username, hashed_password)
			# print(username + hashed_password)

			self.webDatabase.execute(upload_user_string)

		else:
			print("There was a problem uploading {0}, namely it already exists and wasn't caught".format(username))



	def getUser(self, new_user_id):
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
		# 1 is True 0 is False, 1 if the name does exist
		command_string_user = ("SELECT 1 FROM webInfo"
							   " WHERE user_name='{0}';".format(username)
							  )
		
		true_user = self.webDatabase.fetch_one_execute(command_string_user)
		if true_user is not None:
			return True

		return False



	def setPassword(self, password):
		
		return generate_password_hash(password)



	def checkPassword(self, username, password):
		password_hash_string = ("SELECT password_hash FROM webInfo"
								" WHERE user_name='{0}';").format(username)
		password_hash = self.webDatabase.fetch_one_execute(password_hash_string)
		if password_hash is not None:
			password_hash = self.webDatabase.fetch_one_execute(password_hash_string)[0]
			return check_password_hash(password_hash, password)

		return False



	def topTenScores(self):
		show_scores_string = ("SELECT * FROM gameInfo"
							  " ORDER BY tiles DESC"
							  " LIMIT 10;"
							 )
		top_ten = self.webDatabase.fetch_all_execute(show_scores_string)
		return top_ten


	def topTenScoresForPlayer(self, username):
		show_scores_string = ("SELECT * FROM gameInfo"
							  " WHERE player_name='{0}'"
							  " ORDER BY tiles DESC"
							  " LIMIT 10;".format(username)
							 )
		top_ten = self.webDatabase.fetch_all_execute(show_scores_string)
		if top_ten is not None:
			return top_ten

		else:
			return ("None", "None", "None", 0, 0)








class User(UserMixin):
	def __init__(self, username):
		self.username = username
		super().__init__()
		self.id = self.getUserID()

	def getUserID(self):
		get_rowID_string = ("SELECT rowid FROM webInfo"
							" WHERE user_name='{0}';".format(self.username)
							)
		user_ID = DataBase("engine.db").fetch_one_execute(get_rowID_string)

		if user_ID is not None:
			return user_ID[0]
		else:
			return -1

	def checkUser(self):
		print("Check User")

	# def get(new_id):
	# 	if new_id == self.id:
	# 		return self

	# 	else:
	# 		return None










# 	id = db.Column(db.Integer, primary_key = True)
# 	username = db.Column(db.String(64), index = True, unique = True)
# 	email = db.Column(db.String(120), index = True, unique = True)
# 	password_hash = db.Column(db.String(128))
# 	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

# 	def __repr__(self):
# 		return '<User {}>'.format(self.username)

# 	def set_password(self, password):
# 		self.password_hash = generate_password_hash(password)

# 	def check_password(self, password):
# 		return check_password_hash(self.password_hash, password)


# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	body = db.Column(db.String(140))
# 	timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 	def __repr__(self):
# 		return '<Post {}>'.format(self.body)


# @login.user_loader
# def load_user(id):
# 	return User.query.get(int(id))

# db.create_all()







# 	def submitGame(self):
# 		conn = sqlite3.connect('gameEngine.db')

# 		c = conn.cursor()

# 		# Create the table if it doesn't already exist
# 		c.execute(''' CREATE TABLE IF NOT EXISTS game
# 			(game_id integer PRIMARY KEY,
# 			 player_name text NOT NULL,
# 			 character_name text NOT NULL,
# 			 class text NOT NULL
# 			 level integer NOT NULL,
# 			 tiles integer NOT NULL)''')

# 		game_info = (self.player.get_player_name(), self.player.get_character_name(),\
# 			self.player.get_character_class(), self.player.get_character_level(), World.how_many_tile())

# 		c.execute('INSERT INTO game VALUES(?,?,?,?,?)', game_info)





# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()