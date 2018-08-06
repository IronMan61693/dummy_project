#!/usr/bin/env python3

import random

from World import WorldClass
from createPlayer import Player



class playClass():
	"""
	An engine holding the game itself.

	Variables:
		player <Player>
		world <WorldClass>
		room <MapTile>
		new_input <str>
		action_check <bool>
		moved <bool>

	Methods:
		change_player_info() Updates player character info
		enterRoom() Player enters room and world is used to describe if the tile exists
		doAction() If room modifies player does so, then reads in the player's input and does action
		getTileDescription() Returns MapTile intro_text string
		getAvailableActions() Returns MapTile available_actions list
		getTypeOfRoom() Returns room_type int
		setNotMoved() Changes moved bool to False
		getMoved() Returns moved bool
		unstickCharacter() Uses player move to random direction 
		setUserAction() Sets new_input string to input
		submitGameInfo() Returns tuple with game info
		currentInventoryDictionary() Returns inventory dictionary
		currentEquippedAll() Returns inventory get_all_equipped
		equipMainHand() Sets player weapon equal to equipped main hand in inventory
		mainHandOptions() Returns list of Weapons with main hand bool True
		inCombat() Returns bool for room tile in combat
		combatInformation() Returns combat string for the player
		enemyCombatInformation() Returns combat string for the enemy
	"""

	def __init__ (self):

		# Instantiates the player class
		self.player = Player()

		# Loads the world map
		self.world = WorldClass(self.player)


		# Places the player in the associated room(starting) and prints the text
		self.room =  self.world.tile_exists(self.player.location_x, self.player.location_y)

		self.new_input = "None"
		self.action_check = True

		self.moved = True



	def change_player_info(self, class_name, character_name, player_name):
		"""
		Updates player character info

		Input:
			class_name <str>
			character_name <str>
			player_name <str>
		"""
		self.player.set_character_class(class_name)
		self.player.set_character_name(character_name)
		self.player.set_player_name(player_name)	



	def enterRoom(self):
		"""
		Player enters room and world is used to describe if the tile exists
		"""


		# Sets the room = player x,y location
		if (self.world.tile_exists(self.player.location_x, self.player.location_y)):
			self.room = self.world.tile_exists(self.player.location_x, self.player.location_y)

		else:
			self.world.generate_world(self.player.location_x, self.player.location_y)
			self.room =  self.world.tile_exists(self.player.location_x, self.player.location_y)

		

		available_actions = self.room.available_actions()



	
	def doAction(self):
		"""
		If room modifies player does so, then reads in the player's input and does action
		"""	
		# Chack the player's state
		if self.player.is_alive() and self.action_check:

				# Runs room modifications on player if there are any and describes the room
			self.room.modify_player()
			self.action_check = False


			

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
				self.action_check = True
				break

		available_actions = self.room.available_actions()


	def getTileDescription(self):
		"""
		Returns MapTile intro_text string

		Output:
			<str>
		"""
		return self.room.intro_text()

	def getAvailableActions(self):
		"""
		Returns MapTile available_actions list

		Output:
			[<Action>]
		"""
		return self.room.available_actions()

	def getTypeOfRoom(self):
		"""
		Returns MapTile room_type int

		Output:
			<int>
		"""
		return self.room.room_type

	def setNotMoved(self):
		"""
		Changes moved bool to False
		"""
		self.moved = False

	def getMoved(self):
		"""
		Returns moved variable

		Output:
			<bool>
		"""
		return self.moved

	def unstickCharacter(self):
		"""
		Uses player move to random direction 
		"""
		randx = random.randint(-10,10)
		randy = random.randint(-10,10)
		self.player.move(randx, randy)


	def setUserAction(self, action):
		"""
		Sets new_input string to input

		Input:
			action <str>
		"""
		self.new_input = action


	def submitGameInfo(self):
		"""
		Returns tuple with game info

		Output:
			infoTuple(<str>,<str>,<str>,<int>,<int>)
		"""
		self.infoTuple = (self.player.get_player_name(), self.player.get_character_name(),\
						  self.player.get_character_class(), self.player.get_character_level(),\
						  self.world.how_many_tile())


		return self.infoTuple

	def currentInventoryDictionary(self):
		"""
		Returns inventory dictionary

		Output:
			{<Item> : <int>}
		"""
		return self.player.inventory.get_inventory_dict()

	def currentEquippedAll(self):
		"""
		Returns inventory all equipped

		Output:
			(<Weapon>, <bool>, <bool>, <bool>, <bool>)
		"""
		return self.player.inventory.get_all_equipped()

	def equipMainHand(self, weapon):
		"""
		Sets player weapon equal to equipped main hand in inventory
		"""
		if self.player.inventory.equip_main_hand(weapon):
			self.player.weapon = self.player.inventory.get_main_hand_equipped()

	def mainHandOptions(self):
		"""
		Returns list of Weapons with main hand bool True

		Output:
			<bool>
		"""
		return self.player.inventory.get_main_hand_options()

	def inCombat(self):
		"""
		Returns bool for room tile in combat

		Output:
			<bool>
		"""
		return self.room.get_combat()

	def combatInformation(self):
		"""
		Returns combat string for the player

		Output:
			<str>
		"""
		return self.room.enemyCombat.player_combat_string

	def enemyCombatInformation(self):
		"""
		Returns combat string for the enemy

		Output:
			<str>
		"""
		return self.room.enemyCombat.enemy_combat_string

