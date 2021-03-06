import Items, Enemies, Actions, World
import random

class MapTile:
	"""
	Abstract Base class for map locations described in x,y coordinate plane
	 We do not want this to be called directly

	Variables:
		x <int>
		y <int>

	Methods:
		intro_text(self) All map Tiles will want to explain what is in
		 the tile, but we have the error because we do not want to call
		 this directly, only once it is a subclass
		modify_player(self, player) For subclasses to allow modification
		 of player class
		adjacent_move() returns a list of possible directions the player can move
		available_actions() returns a list of actions player can take in this room
	"""
	def __init__(self, x, y):
		"""
		Input: 
			x <int>
			y <int>
		"""
		self.x = x
		self.y = y

	def intro_text(self):
		"""
		Architecture for subclass, describes the tile as string

		Output: 
			raise Error
		"""
		raise NotImplementedError()

	def modify_player(self, player):
		"""
		Architecture for subclass, modifies the input player class

		Output: 
			raise Error
		"""
		raise NotImplementedError()

	def adjacent_moves(self):
		"""
		Describes all actions for adjacent tiles, i.e. where player can move
		 Shuffles the list for the movements and eliminates two of them to give the sense of walls

		Output:
			moves [<Actions>]
		"""
		moves = []

		moves.append(Actions.MoveNorth())

		moves.append(Actions.MoveSouth())

		moves.append(Actions.MoveEast())

		moves.append(Actions.MoveWest())

		random.shuffle(moves)

		moves.pop()

		moves.pop()


		return moves



	def available_actions(self):
		"""
		Describes all methods Actions can call in this room
		 Is default behavior, different tiles(subclasses) will specify more actions

		Output:
			moves [<Actions>]
		"""
		moves = self.adjacent_moves()
		moves.append(Actions.ViewInventory())
		moves.append(Actions.ViewCharacter())
		moves.append(Actions.Quit())

		return moves



class StartingRoom(MapTile):
	"""
	A subclass of the MapTile as the starting room

	Variables:
		player <Player>

	Methods:
		intro_text(self) Describes the room
	"""
	def intro_text(self):
		"""
		Describes the intro tile as string

		Output: 
			intro_description <str>
		"""
		intro_description = ("You have found yourself in a dark cave with a flickering torch on the wall.\n"\
							"There are four paths you see in front of you, each equally dark and foreboding.\n")
		return intro_description

	def modify_player(self, player):
		"""
		This tile does not modify the player, pass
		"""
		pass

	def adjacent_moves(self):
		"""
		Describes all actions for adjacent tiles, i.e. where player can move

		Output:
			moves [<Actions>]
		"""
		moves = []

		moves.append(Actions.MoveNorth())

		moves.append(Actions.MoveSouth())

		moves.append(Actions.MoveEast())

		moves.append(Actions.MoveWest())

		return moves



class LootRoom(MapTile):
	"""
	A subclass of MapTile, a room containing loot

	Variables:
		x <int>
		y <int>
		item <Item>

	Methods:
		add_loot(player) appends loot item to player invetory
		modify_player(player) calls add_loot method
	"""
	def __init__(self, x, y, item):
		"""
		Input:
			x <int>
			y <int>
			item <Item>
		"""
		self.item = item
		super().__init__(x,y)

	def add_loot(self, player):
		"""
		Adds loot to player inventory

		Input:
			player <Player>
		"""
		if self.item.is_looted():
			pass

		else:
			player.inventory.append(self.item)
			self.item.set_looted()

	def modify_player(self, player):
		"""
		Calls add_loot method
		"""
		self.add_loot(player)



class LootCoinRoom(MapTile):
	"""
	A subclass of MapTile, a room containing loot

	Variables:
		x <int>
		y <int>
		item <Item>

	Methods:
		add_loot(player) appends loot item to player invetory
		modify_player(player) calls add_loot method
	"""
	def __init__(self, x, y, coin):
		"""
		Input:
			x <int>
			y <int>
			coin <Item>
		"""
		self.coin = coin
		super().__init__(x,y)

	def add_loot(self, player):
		"""
		Adds loot to player inventory

		Input:
			player <Player>
		"""
		if self.coin.is_looted():
			pass

		else:
			player.add_to_pouch(self.coin.name, self.coin.coin_amount)
			self.coin.set_looted()

	def modify_player(self, player):
		"""
		Calls add_loot method
		"""
		self.add_loot(player)



class EnemyRoom(MapTile):
	"""
	A subclass of MapTile, contains an enemy

	Variables:
		x <int>
		y <int>
		enemy <Enemy>
		the_player <Player>

	Methods:
		modify_player() Enemy attacks the player
		available_actions() adds some actions to be available to use for the player
	"""
	def __init__(self, x, y, enemy):
		"""
		Input:
			x <int>
			y <int>
			enemy <Enemy>
		Output:
			None
		"""
		self.enemy = enemy 
		super().__init__(x, y)

	def modify_player(self, the_player):
		"""
		Continually attacks the player with the enemy 
		 while the enemy is alive

		Input:
			the_player <Player>
		"""	
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("{} enemy does {} damage. You now have {} HP remaining\n".format(self.enemy.name, self.enemy.damage, the_player.hp))

	def available_actions(self):
		"""
		Changes the base available actions, 
		 if the enemy is alive only allow the player to attack or flee
		 otherwise the default moves
		"""
		if self.enemy.is_alive():
			return [Actions.Flee(tile=self), Actions.Attack(enemy = self.enemy)]

		else:
			moves = self.adjacent_moves()
			moves.append(Actions.ViewInventory())
			moves.append(Actions.Quit())

			return moves


class EmptyCavePath(MapTile):
	"""
	A subclass of MapTile, contains nothing unique

	Variables:
		x <int>
		y <int>

	Methods:
		intro_text describes the room
	"""
	def intro_text(self):
		"""
		Describes the tile with string

		Output: 
			intro_description <str>
		"""
		intro_description = ("An unremarkable part of the cave.\n"\
							"You must forge on.\n")
		return intro_description

	def modify_player(self, player):
		"""
		This tile does not modify the player, pass
		"""
		pass



class GiantSpiderRoom(EnemyRoom):
	"""
	A subclass of EnemyRoom, contains a GiantSpider

	Variables:
		x <int>
		y <int>

	Methods:
		modify_player() Enemy attacks the player
	"""
	def __init__(self, x, y):
		super().__init__(x,y,Enemies.GiantSpider())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			intro_description = ("A Giant Spider slides down its web in front of you!\n"\
								 "Ready yourself for battle.\n")

		else:
			intro_description = ("The corpse of the dead spider rots on the ground!\n")

		return intro_description



class OgreRoom(EnemyRoom):
	"""
	A subclass of EnemyRoom, contains an Ogre

	Variables:
		x <int>
		y <int>

	Methods:
		modify_player() Enemy attacks the player
	"""
	def __init__(self,x,y):
		super().__init__(x,y,Enemies.Ogre())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			intro_description = ("A disgusting huge Ogre blocks your way!\n"\
								 "Ready yourself for battle.\n")

		else:
			intro_description = ("The corpse of the massive ogre makes the room reek, gross.\n")

		return intro_description



class FindDaggerRoom(LootRoom):
	"""
	A subclass of LootRoom, contains a dagger

	Variables:
		x <int>
		y <int>

	Methods:

	"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Dagger())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("Is that something shiny in the corner?\n"\
							 	 "Nope, you already found a dagger!\n")
		else:
			
			intro_description = ("Is that something shiny in the corner?\n"\
							 	 "It is! You found a dagger!\n")


		return intro_description



class Find5GoldRoom(LootCoinRoom):
	"""
	A subclass of LootRoom, contains 5 gold

	Variables:
		x <int>
		y <int>

	Methods:

	"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(5))

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.coin.is_looted()):

			intro_description = ("You think there was once some gold in here\n")
		else:
			
			intro_description = ("It seems you have found some loot!\n"\
							 	 "Nice you got 5 gold\n")

		return intro_description



class FindRockRoom(LootRoom):
	"""
	A subclass of LootRoom, contains a rock

	Variables:
		x <int>
		y <int>

	"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Rock())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("There are other rocks, but none quite like the rock you found here\n")

		else:
			
			intro_description = ("A rock sits in the middle of the room.\n"\
							 	 "You begrudgingly pick it up.\n")

		return intro_description



class LeaveCaveRoom(MapTile):
	"""
	A subclass of MapTile, the exit
	 sets victory condition to true
	"""
	def intro_text(self):
		"""
		Describes the tile with string

		Output: 
			intro_description <str>
		"""
		intro_description = ("You see a bright light in the distance...\n"\
							"Could it be, is it growing as you get closer?\n"\
							"It is! It's sunlight!\n\n\n"\
							"Victory has been achieved!!!")
		return intro_description

	def modify_player(self, the_player):
		"""
		This tile does not modify the player, pass
		"""
		the_player.victory = True
