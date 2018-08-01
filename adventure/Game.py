#!/usr/bin/env python3

import random

from World import WorldClass
from createPlayer import Player



class playClass():

	def __init__ (self):

		# Instantiates the player class
		self.player = Player()

		# Loads the world map
		self.world = WorldClass()


		# Places the player in the associated room(starting) and prints the text
		self.room =  self.world.tile_exists(self.player.location_x, self.player.location_y)

		self.new_input = "None"

		self.moved = True



	def change_player_info(self, class_name, character_name, player_name):
		self.player.set_character_class(class_name)
		self.player.set_character_name(character_name)
		self.player.set_player_name(player_name)	



	def enterRoom(self):
		"""
		A loop to have the game continue until player is no longer alive or wins
		"""
		######################################################################################################
		# Load the instances of the world and player
		######################################################################################################

		
		# print(self.room.intro_text())

		######################################################################################################
		# While loop for continual gameplay
		######################################################################################################


		# Sets the room = player x,y location
		if (self.world.tile_exists(self.player.location_x, self.player.location_y)):
			self.room = self.world.tile_exists(self.player.location_x, self.player.location_y)

		else:
			self.world.generate_world(self.player.location_x, self.player.location_y)
			self.room =  self.world.tile_exists(self.player.location_x, self.player.location_y)

		

		available_actions = self.room.available_actions()



	
	def doAction(self):
	
		# Chack the player's state
		if self.player.is_alive() and not self.player.victory:

				# Runs room modifications on player if there are any and describes the room
			self.room.modify_player(self.player)
			

		# Print for Game over
		if not self.player.is_alive():
			
			print("GAME OVER!!!!!\n")
			print("You made it {} tiles this attempt!".format(self.world.how_many_tile()))
			self.world.game_over_room(self.player.location_x, self.player.location_y)
			self.room = self.world.tile_exists(self.player.location_x, self.player.location_y)


			######################################################################################################
			# Player input
			######################################################################################################

		# I dont think I need the print statements here, keeping them in for testing in command line
		print("Choose your action adventurer: \n")

		available_actions = self.room.available_actions()

		# Show which actions the player can perform
		for action in available_actions:
			print(action)

		

		# Verifies the action is one that corresponds to a key
		for action in available_actions:
			if self.new_input == action.hotkey:
				if action.moved:
					self.moved = True

				else:
					self.moved = False					

				self.player.do_action(action, **action.kwargs)
				break


	def getTileDescription(self):
		return self.room.intro_text()

	def getAvailableActions(self):
		return self.room.available_actions()

	def getTypeOfRoom(self):
		return self.room.room_type

	def setNotMoved(self):
		self.moved = False

	def getMoved(self):
		return self.moved

	def unstickCharacter(self):
		randx = random.randint(-10,10)
		randy = random.randint(-10,10)
		self.player.move(randx, randy)


	def setUserAction(self, action):
		self.new_input = action


	def submitGameInfo(self):
		self.infoTuple = (self.player.get_player_name(), self.player.get_character_name(),\
						  self.player.get_character_class(), self.player.get_character_level(),\
						  self.world.how_many_tile())


		return self.infoTuple

	def currentInventoryDictionary(self):
		return self.player.inventory.get_inventory_dict()

	def currentEquippedAll(self):
		return self.player.inventory.get_all_equipped()

	def equipMainHand(self, weapon):
		self.player.inventory.equip_main_hand(weapon)

	def mainHandOptions(self):
		return self.player.inventory.get_main_hand_options()


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