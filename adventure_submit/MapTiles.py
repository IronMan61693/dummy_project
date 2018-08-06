import Items, Enemies, Actions
import random
from combat import Combat

class MapTile:
	"""
	Abstract Base class for map locations described in x,y coordinate plane
	 We do not want this to be called directly

	Variables:
		x <int>
		y <int>
		player <Player>
		room_type <int>
		adjacent_movements [<Actions>]
		all_moves [<Actions>]
		combat <bool>

	Methods:
		get_combat() Returns combat variable
		intro_text() All map Tiles will want to explain what is in
		 the tile, but we have the error because we do not want to call
		 this directly, only once it is a subclass
		modify_player() For subclasses to allow modification
		 of player class
		adjacent_moves() Returns a list of possible directions the player can move
		set_available_actions () Appends actions to all_moves
		available_actions() Returns a list of actions player can take in this room
	"""
	def __init__(self, x, y, player):
		self.x = x
		self.y = y
		self.player = player
		self.room_type = 0
		self.adjacent_movements = self.adjacent_moves()
		self.all_moves = []
		self.set_available_actions()
		self.combat = False



	def get_combat(self):
		"""
		Returns combat variable

		Output:
			combat <bool>
		"""
		return self.combat




	def intro_text(self):
		"""
		Architecture for subclass, describes the tile as string

		Output: 
			raise Error
		"""
		raise NotImplementedError()

	def modify_player(self):
		"""
		Architecture for subclass, modifies the input player class

		Output: 
			raise Error
		"""
		raise NotImplementedError()

	
	def adjacent_moves(self):
		"""
		Determines which of the 4 directions the player can move in, i.e. where player can move

		Output:
			moves [<Actions>]
		"""
		moves = []

		moves.append(Actions.MoveNorth())

		moves.append(Actions.MoveSouth())

		moves.append(Actions.MoveEast())

		moves.append(Actions.MoveWest())


		random.shuffle(moves)

		remove_move = random.randint(0, 3)

		for removed in range(0, remove_move):

			moves.pop()


		return moves


	def set_available_actions(self):
		"""
		Appends actions to all_moves
		"""
		self.all_moves = self.adjacent_movements
		self.all_moves.append(Actions.ViewInventory())
		self.all_moves.append(Actions.Equip())
		self.all_moves.append(Actions.ViewCharacter())
		# self.all_moves.append(Actions.Quit())



	def available_actions(self):
		"""
		Returns all_moves

		Output:
			moves [<Actions>]
		"""
				

		return self.all_moves



class StartingRoom(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() For subclasses to allow modification
			 of player class
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			available_actions() Returns a list of actions player can take in this room
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

	def modify_player(self):
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



class GameOverRoom(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() For subclasses to allow modification
			 of player class
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
	"""
	def intro_text(self):
		"""
		Describes the intro tile as string

		Output: 
			intro_description <str>
		"""
		self.room_type = -1
		intro_description = ("You have found yourself unable to go on.\n"\
							 "Good Game\n")
		return intro_description

	def modify_player(self):
		"""
		This tile does not modify the player, pass
		"""
		pass

	def set_available_actions(self):
		"""
		Appends Actions to all_moves
		"""
		self.all_moves.append(Actions.ViewInventory())
		self.all_moves.append(Actions.ViewCharacter())
		# self.all_moves.append(Actions.Quit())



class LootRoom(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
		item <Item>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
		add_loot() If the room has not be looted adds the item to player's inventory
	"""
	def __init__(self, x, y, player, item):
		self.item = item
		super().__init__(x,y, player)

		self.room_type = 1

	def add_loot(self):
		"""
		If the room has not be looted adds the item to player's inventory
		"""
		if self.item.is_looted():
			pass

		else:
			self.player.inventory.add_to_inventory(self.item, 1)
			self.item.set_looted()
			self.room_type = 2

	def modify_player(self):
		"""
		Calls add_loot method
		"""
		self.add_loot()



class LootCoinRoom(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
		coin <Coin>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
		add_loot() If the room has not be looted adds the Coin to player's inventory
	"""
	def __init__(self, x, y, player, coin):
		"""
		Input:
			x <int>
			y <int>
			coin <Item>
		"""
		self.coin = coin
		super().__init__(x,y, player)

		self.room_type = 1

	def add_loot(self):
		"""
		Adds loot to player inventory
		"""
		if self.coin.is_looted():
			pass

		else:
			self.room_type = 2
			self.player.inventory.add_to_pouch(self.coin.name, self.coin.coin_amount)
			self.coin.set_looted()

	def modify_player(self):
		"""
		Calls add_loot method
		"""
		self.add_loot()



class EnemyRoom(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
		enemy <Enemy>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Enemy attacks the player
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
	"""
	def __init__(self, x, y, player, enemy):
		self.enemy = enemy 
		self.enemyCombat = Combat(player, self.enemy)
		super().__init__(x, y, player)

		

		self.combat = True
		
		self.room_type = 3
		self.update_available_actions = True

			
	def modify_player(self):
		"""
		Continually attacks the player with the enemy 
		 while the enemy is alive
		"""	
		if self.enemy.is_alive():
			
			self.enemyCombat.enemy_attack()
			combat_string = self.enemyCombat.combat_description()

		else:
			self.room_type = 4
			if (self.update_available_actions):
				self.set_available_actions()
				self.update_available_actions = False
				self.combat = False
				


	def set_available_actions(self):
		"""
		Changes the base available actions, 
		 if the enemy is alive only allow the player to attack or flee
		 otherwise the default moves
		"""
		if self.enemy.is_alive():
			self.all_moves = [Actions.Flee(tile=self), Actions.Attack(combatClass = self.enemyCombat)]
			self.all_moves.append(Actions.ViewInventory())
			self.all_moves.append(Actions.Equip())
			self.all_moves.append(Actions.ViewCharacter())
			# self.all_moves.append(Actions.Quit())



		else:
			self.all_moves = self.adjacent_movements
			self.all_moves.append(Actions.ViewInventory())
			self.all_moves.append(Actions.Equip())
			self.all_moves.append(Actions.ViewCharacter())
			# self.all_moves.append(Actions.Quit())





 


class EmptyCavePath(MapTile):
	"""
	A subclass of the MapTile

	Variables:
		Inherited from MapTile:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Enemy attacks the player
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
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

	def modify_player(self):
		"""
		This tile does not modify the player, pass
		"""
		pass



class GiantSpiderRoom(EnemyRoom):
	"""
	A subclass of the EnemyRoom

	Variables:
		Inherited from EnemyRoom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			enemy <Enemy>

	Methods:
		Inherited from EnemyRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Enemy attacks the player
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
	"""
	def __init__(self, x, y, player):
		super().__init__(x,y, player, Enemies.GiantSpider())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 5
			intro_description = ("A Giant Spider slides down its web in front of you!\n"\
								 "Ready yourself for battle.\n")

		else:
			self.room_type = 6
			intro_description = ("The corpse of the dead spider rots on the ground!\n")

		return intro_description



class OgreRoom(EnemyRoom):
	"""
	A subclass of the EnemyRoom

	Variables:
		Inherited from EnemyRoom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			enemy <Enemy>

	Methods:
		Inherited from EnemyRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Enemy attacks the player
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
	"""
	def __init__(self,x,y, player):
		super().__init__(x,y, player, Enemies.Ogre())

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
	A subclass of the LootRoom

	Variables:
		Inherited from LootRoom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			item <Item>

	Methods:
		Inherited from LootRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			add_loot() If the room has not be looted adds the item to player's inventory
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.Dagger())

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
	A subclass of the LootRoom

	Variables:
		Inherited from LootRoom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			item <Item>

	Methods:
		Inherited from LootRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			add_loot() If the room has not be looted adds the item to player's inventory
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.Gold(5))

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



class FindShortSwordRoom(LootRoom):
	"""
	A subclass of the LootRoom

	Variables:
		Inherited from LootRoom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			item <Item>

	Methods:
		Inherited from LootRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			add_loot() If the room has not be looted adds the item to player's inventory
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.ShortSword())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("This room reminds you of that time you found a short sword here.\n")

		else:
			
			intro_description = ("A short sword is stabbed in something gooey in the middle of the room.\n"\
							 	 "You begrudgingly pick it up, gross.\n")

		return intro_description



# class LeaveCaveRoom(MapTile):
# 	"""
# 	A subclass of MapTile, the exit
# 	 sets victory condition to true
# 	"""
# 	def intro_text(self):
# 		"""
# 		Describes the tile with string

# 		Output: 
# 			intro_description <str>
# 		"""
# 		intro_description = ("You see a bright light in the distance...\n"\
# 							"Could it be, is it growing as you get closer?\n"\
# 							"It is! It's sunlight!\n\n\n"\
# 							"Victory has been achieved!!!")
# 		return intro_description

# 	def modify_player(self, the_player):
# 		"""
# 		This tile does not modify the player, pass
# 		"""
# 		the_player.victory = True
