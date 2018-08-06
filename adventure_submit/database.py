import sqlite3

class DataBase(object):
	"""
	A class to simplify database interactions

	Variables:
		database_name <str>

	Methods:
		connect () establishes a sqlite connection to the database passed in through init
		close () closes the connection
		execute() runs sqlite execute on the command string passed in, the tuple increases security 
		 by not passing in variables directly
		fetch_one_execute() runs like execute but returns a fetch one command on any select statement commands
		fetch_all_execute() runs like execute but returns a fetch all command on any select statement commands

	"""

	def __init__(self, database_name = "database.db"):

		self.database_name = database_name
		self.connect()

	def connect(self):
		"""
		Uses sqlite to establish a connection with a database defined in the init

		Output:
			Connection established
		"""

		self.connection = sqlite3.connect(self.database_name, check_same_thread = False)
		self.cursor = self.connection.cursor()
		self.connected = True

	def close(self):
		"""
		Uses sqlite to close the connection

		Output:
			Connection closed
		"""

		self.connection.commit()
		self.connection.close()
		self.connected = False


	def execute(self, commands, tupleParameter = ()):
		"""
		A very simple execute method that takes in a list of commands and executes 
		 them, the tuple is used to pass in variables
		 Error handling and bad commands TBD

		Input:
			commands [str]
			tupleParameter (str)

		Output:
			Executes on database
		"""

		close = False
		if not self.connected:
			# Open a previously closed connection if closed
			self.connect()
			# Mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			# All commands are dealt with in a list
			commands = [commands]

		for command in commands:

			self.cursor.execute(command, tupleParameter)

		# Commits after all commands have been executed
		self.connection.commit()

		if close:
			self.close()

	def fetch_one_execute(self, commands, tupleParameter = ()):
		"""
		A very simple execute method that takes in a list of commands and executes 
		 them, the tuple is used to pass in variables
		 Error handling and bad commands TBD

		Input:
			commands [str]
			tupleParameter (str)

		Output:
			Executes on database
			return fetchone <str>
		"""

		close = False
		if not self.connected:
			# Open a previously closed connection
			self.connect()
			# Mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			#  All commands are dealt with in a list
			commands = [commands]

		for command in commands:

			self.cursor.execute(command, tupleParameter)
			

		# Commits after all commands have been executed
		self.connection.commit()

		if close:
			self.close()

		return self.cursor.fetchone()

	def fetch_all_execute(self, commands, tupleParameter = ()):
		"""
		A very simple execute method that takes in a list of commands and executes 
		 them, the tuple is used to pass in variables
		 Error handling and bad commands TBD

		Input:
			commands [str]
			tupleParameter (str)

		Output:
			Executes on database
			return fetchall [<str>]


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
			# Open a previously closed connection
			self.connect()
			# Mark the connection to be closed once complete
			close = True

		if type(commands) == str:
			#  All commands are dealt with in a list
			commands = [commands]

		for command in commands:
			self.cursor.execute(command, tupleParameter)
			

		self.connection.commit()

		if close:
			self.close()

		return self.cursor.fetchall()