import sqlite3

class DataBase(object):

	def __init__(self, database_name = "database.db"):

		self.database_name = database_name
		self.connect()

	def connect(self):

		self.connection = sqlite3.connect(self.database_name, check_same_thread = False)
		self.cursor = self.connection.cursor()
		self.connected = True

	def close(self):

		self.connection.commit()
		self.connection.close()
		self.connected = False


	def execute(self, commands, tupleParameter = ()):
		"""
		A very simple execute method that takes in a list of commands and executes 
		 them, error handling and bad commands TBD

		Input:
			commands [str]

		Output:
			Executes on database
		"""
		close = False
		if not self.connected:
			#open a previously closed connection
			self.connect()
			#mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			#  All commands are dealt with in a list
			commands = [commands]

		for command in commands:
			# try:
			self.cursor.execute(command, tupleParameter)


			for tup in tupleParameter:
				print("Database: " + str(tup))

			# except sqlite3.Error as error:
			# 	print ("An error occurred:")
			# 	print ("For the command: {}".format(str(command)))

		self.connection.commit()

		if close:
			self.close()

	def fetch_one_execute(self, commands, tupleParameter = ()):
		"""
		A very simple execute method that takes in a list of commands and executes 
		 them, error handling and bad commands TBD

		Input:
			commands [str]

		Output:
			Executes on database
		"""
		close = False
		if not self.connected:
			#open a previously closed connection
			self.connect()
			#mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			#  All commands are dealt with in a list
			commands = [commands]

		for command in commands:
			# try:
			self.cursor.execute(command, tupleParameter)
			

			for tup in tupleParameter:
				print("Database: " + str(tup))

			# except sqlite3.Error as error:
			# 	print ("An error occurred:")
			# 	print ("For the command: {}".format(str(command)))

		self.connection.commit()

		if close:
			self.close()

		return self.cursor.fetchone()

	def fetch_all_execute(self, commands, tupleParameter = ()):
		"""
		Elements can be accessed in the following form
		Recipes = [dict(ID=row[0],
					Title=row[1],
					Picture=row[2],
					Rating=row[3]) for row in cur.fetchall()]
		Gives a list element for each row where the elements are dictionaries
		and the key is ID, Title, Picture, Rating (the columns), and the values
		are the associated values in the database

		If we then want to access this in the html is would look like:
		{% for recipe in Recipes %}
			<strong>ID:</strong> {{ recipe.ID }} <br>
			<strong>Title:</strong> {{ recipe.Title }} <br>
			<strong>Picture:</strong> {{ recipe.Picture }} <br>
			<strong>Rating:</strong> {{ recipe.Rating }} <br>
		{% endfor %}
		"""
		close = False
		if not self.connected:
			#open a previously closed connection
			self.connect()
			#mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			#  All commands are dealt with in a list
			commands = [commands]

		for command in commands:
			# try:
			self.cursor.execute(command, tupleParameter)
			

			for tup in tupleParameter:
				print("Database: " + str(tup))

			# except sqlite3.Error as error:
			# 	print ("An error occurred:")
			# 	print ("For the command: {}".format(str(command)))

		self.connection.commit()

		if close:
			self.close()

		return self.cursor.fetchall()