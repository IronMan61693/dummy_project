import random
from MapTiles import *

class WorldClass(object):
	"""
	A world object to store the game tiles and the player's position
	
	Variables:
		tile_count <int>
		player <Player>
		starting_position (<int>, <int>)
		worldDictionary {(<int>,<int>) : <MapTile>}
		fillTiles [<MapTile>]
		possibleTilesSet {<MapTile>}

	Methods:
		generate_world() Used to generate the tiles if a new tile needs to be generated
		game_over_room() Sets the player to the GameOverRoom game tile
		pick_new_tile() Used to add a tile to the fillTiles list
		how_many_tile() Returns variable tile_count
		tile_exists() Returns the tile for a given x,y coordinate
	"""
	def __init__(self, player):

		# Used to keep track of how many tiles have been placed for adding new tiles and difficulty
		self.tile_count = 1

		self.player = player

		# A tuple holding the x,y grid coordinates
		self.starting_position = (0,0)

		# A dictionary to hold the maptiles making up the world
		# The a (<int>,<int>) tuple is the key representing the location
		# and the value is the tile object
		self.worldDictionary = {}

		# This starts the world dictionary with the StartingRoom tile and coordinates 0,0
		self.worldDictionary[(0, 0)] = StartingRoom(0,0, self.player)

		# A List which holds all of the tiles which can be 
		# pulled from while generating the world
		self.fillTiles = []

		# Originally populating the fillTiles
		self.fillTiles.extend(["Find5GoldRoom"]*8)
		self.fillTiles.extend(["EmptyCavePath"]*8)

		self.fillTiles.extend(["BanditRoom"]*8)
		self.fillTiles.extend(["GiantSpiderRoom"]*6)
		self.fillTiles.extend(["ValkyrieRoom"]*4)
		self.fillTiles.extend(["OgreRoom"]*2)
		self.fillTiles.extend(["AssassinRoom"]*1)
		self.fillTiles.extend(["DeathKnightRoom"]*0)
		self.fillTiles.extend(["GiantRoom"]*0)
		self.fillTiles.extend(["GreenDragonRoom"]*0)
		self.fillTiles.extend(["WizardRoom"]*0)
		
		self.fillTiles.extend(["FindDaggerRoom"]*2)
		self.fillTiles.extend(["FindShortSwordRoom"]*2)
		self.fillTiles.extend(["FindQuarterStaffRoom"]*2)
		self.fillTiles.extend(["FindLongSwordRoom"]*2)
		self.fillTiles.extend(["FindBattleAxeRoom"]*2)

		self.fillTiles.extend(["FindPaddedClothRoom"]*2)
		self.fillTiles.extend(["FindStuddedLeatherRoom"]*2)
		self.fillTiles.extend(["FindChainShirtRoom"]*2)
		self.fillTiles.extend(["FindRingMailRoom"]*2)
		self.fillTiles.extend(["FindFullPlateRoom"]*2)


		self.fillTiles.extend(["HealRoomWeak"]*1)
		self.fillTiles.extend(["HealRoomMedium"]*1)
		self.fillTiles.extend(["HealRoomStrong"]*1)
		self.fillTiles.extend(["HealRoomSuperior"]*1)
		self.fillTiles.extend(["HealRoomExtreme"]*0)



		# Used to fill in to fillTiles when fillTiles pops
		self.possibleTilesSet = {"Find5GoldRoom", "EmptyCavePath",\
								 "BanditRoom", "GiantSpiderRoom", "ValkyrieRoom",\
								 "OgreRoom", "AssassinRoom", "DeathKnightRoom",\
								 "GiantRoom", "GreenDragonRoom", "WizardRoom",\
								 "FindShortSwordRoom", "FindDaggerRoom", "FindQuarterStaffRoom",\
								 "FindLongSwordRoom", "FindBattleAxeRoom",\
								 "FindPaddedClothRoom", "FindStuddedLeatherRoom",\
								 "FindMoonSwordRoom",\
								 "FindChainShirtRoom", "FindRingMailRoom", "FindFullPlateRoom",\
								 "HealRoomWeak", "HealRoomMedium", "HealRoomStrong",\
								 "HealRoomSuperior", "HealRoomExtreme"}




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
			self.worldDictionary[(x, y)] = getattr(__import__('MapTiles'), self.pick_new_tile()) (x,y, self.player)


	def game_over_room(self, x, y):
		"""
		Sets the player to the GameOverRoom game tile

		Input:
			x <int>
			y <int>
		"""
		self.worldDictionary[(x, y)] = GameOverRoom(x,y, self.player)


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
		"""
		Returns variable tile_count

		Output:
			tile_count <int>
		"""
		return self.tile_count




	def tile_exists(self, x, y):
		"""
		Check if there is a tile at the coordinate x,y

		Input:
			x <int>
			y <int>

		Output:
			value of x,y key in world dict <MapTile>
		"""
		return self.worldDictionary.get((x,y))
