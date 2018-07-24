#!/usr/bin/env python3

from time import sleep

import World
from createPlayer import Player

def change_player_class(change_player, class_name):
	change_player.set_character_class(class_name)

class playClass():

	def __init__ (self, player_class_name):

		# Instantiates the player class
		self.player = Player()
		change_player_class(self.player, player_class_name)

		# Loads the world map
		World.initialize_world()


		# Places the player in the associated room(starting) and prints the text
		self.room = World.tile_exists(self.player.location_x, self.player.location_y)

		self.new_input = "None"
		self.inputreceived = 0

	def play(self):
		"""
		A loop to have the game continue until player is no longer alive or wins
		"""
		######################################################################################################
		# Load the instances of the world and player
		######################################################################################################

		
		print(self.room.intro_text())

		######################################################################################################
		# While loop for continual gameplay
		######################################################################################################

		while self.player.is_alive() and not self.player.victory:


			# Sets the room = player x,y location
			if (World.tile_exists(self.player.location_x, self.player.location_y)):
				self.room = World.tile_exists(self.player.location_x, self.player.location_y)

			else:
				self.room = World.generate_world(self.player.location_x, self.player.location_y)

			# Runs room modifications on player if there are any and describes the room
			self.room.modify_player(self.player)

			# Print for Game over
			if not self.player.is_alive():
				
				print("GAME OVER!!!!!\n")
				print("You made it {} tiles this attempt!".format(World.how_many_tile()))

			# Chack the player's state
			if self.player.is_alive() and not self.player.victory:

				######################################################################################################
				# Player input
				######################################################################################################

				print("Choose your action adventurer: \n")

				available_actions = self.room.available_actions()

				# Show which actions the player can perform
				for action in available_actions:
					print(action)

				
				# self.action_input = input("Action:\n")
				# Use huge sleep number  and then a function that kicks out of sleep?
				if self.inputreceived == 0:
					for i in range (10000):
						sleep(1)
						if self.inputreceived ==1:
							break

				if self.new_input != "None":
					print(self.new_input)
				

				# Verifies the action is one that corresponds to a key
				for action in available_actions:
					if self.new_input == action.hotkey:
						self.player.do_action(action, **action.kwargs)
						self.inputreceived = 0
						break

				self.inputreceived = 0

	def getTileDescription(self):
		return self.room.intro_text()

	def getAvailableActions(self):
		return self.room.available_actions()

	def setUserAction(self, action):
		self.new_input = action
		self.inputreceived =1





