import random

# A dictionary to hold the maptiles making up the world
# The a (<int>,<int>) tuple is the key representing the location
# and the value is the tile object
_world = {}

# A List which holds all of the tiles which can be 
# pulled from while generating the world
# This lets me initialize the new_world list
new_world = []
new_world.extend(["Find5GoldRoom"]*4)
# new_world.extend(["EmptyCavePath"]*12)
# new_world.extend(["OgreRoom"]*2)
# new_world.extend(["GiantSpiderRoom"]*4)
# new_world.extend(["FindRockRoom"]*3)
# new_world.extend(["FindDaggerRoom"]*2)
# new_world.extend(["LeaveCaveRoom"])

# When an item is popped from the new_world list I will append a new item from this set 
# TBD add difficulty to change item find
possibleTilesSet = {"Find5GoldRoom", "EmptyCavePath", "OgreRoom", "GiantSpiderRoom", "FindRockRoom", "FindDaggerRoom"}


# Used to keep track of how many tiles have been placed for adding new tiles and difficulty
tile_count = 1

# A tuple holding the x,y grid coordinates
starting_position = (0,0)


# Initialize the world with the startingtile at (0,0)
def initialize_world():
	"""	
	This starts the world dictionary with the StartingRoom tile and coordinates 0,0
	"""
	_world[(0, 0)] = getattr(__import__('MapTiles'), "StartingRoom")(0,0)


def generate_world(x, y):
	"""
	This is used to generate the tiles if a new tile needs to be generated

	Input:
		x <int>
		y <int>

	Output:
		adds the key (x,y) to the _world dictionary with the tile object as the value
	"""
	if tile_exists(x, y):
		pass

	else:
		_world[(x, y)] = getattr(__import__('MapTiles'), pick_new_tile()) (x,y)


def pick_new_tile():
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
	random.shuffle(new_world)
	new_tile_name = new_world.pop()
	add_to_list = list(possibleTilesSet)
	random.shuffle(add_to_list)

	new_world.append(add_to_list[0])

	global tile_count

	tile_count += 1

	return new_tile_name


def how_many_tile():
	return tile_count




def tile_exists(x, y):
	"""
	Check if there is a tile at the coordinate x,y

	Input:
		x <int>
		y <int>

	Output:
		value of x,y key in world dict
	"""
	return _world.get((x,y))
