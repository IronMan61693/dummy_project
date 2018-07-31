import random
from MapTiles import *

class WorldClass(object):
	"""
	A world object to store the game tiles and the player's position
	"""
	def __init__(self):
		# Used to keep track of how many tiles have been placed for adding new tiles and difficulty
		self.tile_count = 1

		# A tuple holding the x,y grid coordinates
		self.starting_position = (0,0)

		# A dictionary to hold the maptiles making up the world
		# The a (<int>,<int>) tuple is the key representing the location
		# and the value is the tile object
		self.worldDictionary = {}

		# This starts the world dictionary with the StartingRoom tile and coordinates 0,0
		self.worldDictionary[(0, 0)] = StartingRoom(0,0)

		# A List which holds all of the tiles which can be 
		# pulled from while generating the world
		self.fillTiles = []

		# Originally populating the fillTiles
		self.fillTiles.extend(["Find5GoldRoom"]*4)
		self.fillTiles.extend(["EmptyCavePath"]*12)
		self.fillTiles.extend(["OgreRoom"]*2)
		self.fillTiles.extend(["GiantSpiderRoom"]*4)
		self.fillTiles.extend(["FindRockRoom"]*3)
		self.fillTiles.extend(["FindDaggerRoom"]*2)



		# When an item is popped from the new_world list I will append a new item 
		# from this set TBD add difficulty to change item find
		self.possibleTilesSet = {"Find5GoldRoom", "EmptyCavePath", "OgreRoom", \
								 "GiantSpiderRoom", "FindRockRoom", "FindDaggerRoom"}




	def generate_world(self, x, y):
		"""
		This is used to generate the tiles if a new tile needs to be generated

		Input:
			x <int>
			y <int>

		Output:
			adds the key (x,y) to the _world dictionary with the tile object as the value
		"""
		if self.tile_exists(x, y):
			pass

		else:
			self.worldDictionary[(x, y)] = getattr(__import__('MapTiles'), self.pick_new_tile()) (x,y)


	def game_over_room(self, x, y):

		self.worldDictionary[(x, y)] = GameOverRoom(x,y)


	def pick_new_tile(self):
		"""
		This picks a random tile from the new_world list
		It also adds a new element to the list from the set of all possible tiles so it can go on forever
		TBD Add new tiles to the list at certain increments a different function
		TBD have a list of harder enemies in order, and once the dictionary runs out of a key
		 Add the new harder enemy with a value of like 5 to start taking from
		 Once the list of harder enemies is empty recreate it with a higher difficulty
		
		Output:
			new_tile_name <str>
		"""
		random.shuffle(self.fillTiles)
		new_tile_name = self.fillTiles.pop()
		add_to_list = list(self.possibleTilesSet)
		random.shuffle(add_to_list)

		self.fillTiles.append(add_to_list[0])

		self.tile_count

		self.tile_count += 1

		return new_tile_name


	def how_many_tile(self):
		return self.tile_count




	def tile_exists(self, x, y):
		"""
		Check if there is a tile at the coordinate x,y

		Input:
			x <int>
			y <int>

		Output:
			value of x,y key in world dict
		"""
		return self.worldDictionary.get((x,y))
