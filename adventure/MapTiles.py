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
			self.room_type = 3
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
			self.room_type = 4
			intro_description = ("A disgusting huge Ogre blocks your way!\n"\
								 "Ready yourself for battle.\n")

		else:
			self.room_type = 3
			intro_description = ("The corpse of the massive ogre makes the room reek, gross.\n")

		return intro_description



class BanditRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.Bandit())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 6
			intro_description = ("A bandit is sitting in your path!\n"\
								 "Ready yourself for battle.\n")

		else:
			self.room_type = 3
			intro_description = ("The poor bandit picked the wrong room to wait in.\n")

		return intro_description



class ValkyrieRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.Valkyrie())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 7
			intro_description = ("A burly woman like barbarian charges at you!\n"\
								 "She screams 'Meet the axe of a valkyrie!'\n")

		else:
			self.room_type = 3
			intro_description = ("The burly woman was no match for you!\n")

		return intro_description



class AssassinRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.Assassin())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 8
			intro_description = ("The whisper of cloth catches your attention.\n"\
								 "Then so does the dagger in your back.\n"\
								 "An assassin has attacked you!\n")

		else:
			self.room_type = 3
			intro_description = ("Hopefully the assassin wasn't paid up front.\n")

		return intro_description




class DeathKnightRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.DeathKnight())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 9
			intro_description = ("A large knight in pitch black armor blocks your way.\n"\
								 "You shall not pass he drones.\n")

		else:
			self.room_type = 3
			intro_description = ("The black armor sits eerily now that the knight is dead.\n")

		return intro_description



class GiantRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.Giant())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 10
			intro_description = ("A massive form fills the room.\n"\
								 "It's a giant!\n")

		else:
			self.room_type = 3
			intro_description = ("You still can't believe you killed a giant.\n")

		return intro_description




class GreenDragonRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.GreenDragon())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 11
			intro_description = ("Is that... Could it be... a a a DRAGON\n"\
								 "A green dragon sits before you, amused at your tiny weapon!\n")

		else:
			self.room_type = 3
			intro_description = ("You will have to let everyone know that you killed a dragon.\n")

		return intro_description




class WizardRoom(EnemyRoom):
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
		super().__init__(x,y, player, Enemies.Wizard())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.enemy.is_alive()):
			self.room_type = 12
			intro_description = ("An odd aura fills the room, as an old looking man glances up towards you.\n"\
								 "It's a wizard!\n")

		else:
			self.room_type = 3
			intro_description = ("You bested a master of the arcane in the room.\n")

		return intro_description


















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



class FindQuarterStaffRoom(LootRoom):
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
		super().__init__(x, y, player, Items.QuarterStaff())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("You still see the hand you took your staff from.\n")

		else:
			
			intro_description = ("A quarter staff is still being held by a zombie like hand.\n"\
							 	 "You carefully make the hand let the staff go.\n")

		return intro_description




class FindLongSwordRoom(LootRoom):
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
		super().__init__(x, y, player, Items.LongSword())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("There is a stone which once had a sword.\n")

		else:
			
			intro_description = ("A long sword is currently sealed in a rock.\n"\
							 	 "You yank and it slides right out, that was easy.\n")

		return intro_description


class FindBattleAxeRoom(LootRoom):
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
		super().__init__(x, y, player, Items.BattleAxe())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("The viking is laying dead on the floor, you still have his axe.\n")

		else:
			
			intro_description = ("A terrifying viking charges you!\n"\
							 	 "He slips on the wet floor and dies, you take his axe.\n")

		return intro_description



class FindMoonSwordRoom(LootRoom):
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
		super().__init__(x, y, player, Items.MoonSword())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("The room still feels saturated with the magic of the sword here.\n")

		else:
			
			intro_description = ("An amazing frightful magical aura permeates this room!\n"\
							 	 "You found a glowing sword floating in the room.\n")

		return intro_description











class FindPaddedClothRoom(LootRoom):
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
		super().__init__(x, y, player, Items.PaddedCloth())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("There is a slightly less dusty area where folded cloths used to be.\n")

		else:
			
			intro_description = ("It seems a large pile of clothes are piled in the middle of the room.\n"\
							 	 "Upon picking it up you see it is actually some sort of cloth armor.\n")

		return intro_description

class FindStuddedLeatherRoom(LootRoom):
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
		super().__init__(x, y, player, Items.StuddedLeather())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("Once not so long ago a skeleton had leather armor in this room.\n")

		else:
			
			intro_description = ("A skeleton is wearing some leather armor.\n"\
							 	 "Good thing you aren't above stealing from the dead.\n")

		return intro_description




class FindChainShirtRoom(LootRoom):
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
		super().__init__(x, y, player, Items.ChainShirt())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("You are relieved to know noone was tortured in this room.\n")

		else:
			
			intro_description = ("Is that a torture device hanging from the ceiling?\n"
								 "Ah, nope someone just hung a chain shirt here long ago.\n")

		return intro_description




class FindRingMailRoom(LootRoom):
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
		super().__init__(x, y, player, Items.RingMail())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("There is a nice red stain on the floor where the chain mail you have came from.\n")

		else:
			
			intro_description = ("What are those rusty metal rings over there?\n"
								 "Oh it is a full set of ring mail that is weirdly rusty.\n")

		return intro_description




class FindFullPlateRoom(LootRoom):
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
		super().__init__(x, y, player, Items.FullPlate())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("You remember the oustanding luck to find a complete set of Full Plate here.\n")

		else:
			
			intro_description = ("Wow a conveniently placed set of Full Plate, what are the odds.\n")

		return intro_description














class HealRoom(MapTile):
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
		health_pot <Item>

	Methods:
		Inherited from MapTile:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
		heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player, item):
		self.item = item
		super().__init__(x,y, player)

		self.room_type = 1

	def heal_player(self):
		"""
		If the room has not be looted heals the player
		"""
		if self.item.is_looted():
			pass

		else:
			self.player.hp += self.item.heal_num
			self.item.set_looted()
			self.room_type = 2

	def modify_player(self):
		"""
		Calls add_loot method
		"""
		self.heal_player()



class HealRoomWeak(HealRoom):
	"""
	A subclass of the HealRoom

	Variables:
		Inherited from Healroom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			health_pot <Item>

	Methods:
		Inherited from HealRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.HealingPotionWeak())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("You faintly remember a brief respite here.\n")

		else:

			intro_description = ("A relatively relaxing room that you take a quick break in.\n"\
								 "You are healed for {} during the rest.\n".format(self.item.heal_num))

		return intro_description



class HealRoomMedium(HealRoom):
	"""
	A subclass of the HealRoom

	Variables:
		Inherited from Healroom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			health_pot <Item>

	Methods:
		Inherited from HealRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.HealingPotionMedium())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("This room has a spring you believe you have used already.\n")

		else:

			intro_description = ("A room with a little spring, you clean yourself up and relax.\n"\
								 "You are healed for {} from the cleaning.\n".format(self.item.heal_num))

		return intro_description



class HealRoomStrong(HealRoom):
	"""
	A subclass of the HealRoom

	Variables:
		Inherited from Healroom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			health_pot <Item>

	Methods:
		Inherited from HealRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.HealingPotionStrong())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("There is some shiny glitter from a the fairy you met.\n")

		else:

			intro_description = ("A cute fairy floats in the room.\n"\
								 "You are healed for {} from the generosity of the little folk.\n".format(self.item.heal_num))

		return intro_description



class HealRoomSuperior(HealRoom):
	"""
	A subclass of the HealRoom

	Variables:
		Inherited from Healroom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			health_pot <Item>

	Methods:
		Inherited from HealRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.HealingPotionSuperior())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("A discarded bottle rests in the room.\n")

		else:

			intro_description = ("A potion sits in the room, good thing you will drink strange beverages.\n"\
								 "You are healed for {} from the potion.\n".format(self.item.heal_num))

		return intro_description



class HealRoomExtreme(HealRoom):
	"""
	A subclass of the HealRoom

	Variables:
		Inherited from Healroom:
			x <int>
			y <int>
			player <Player>
			room_type <int>
			adjacent_movements [<Actions>]
			all_moves [<Actions>]
			combat <bool>
			health_pot <Item>

	Methods:
		Inherited from HealRoom:
			get_combat() Returns combat variable
			intro_text() Returns string describing the room
			modify_player() Calls add_loot
			adjacent_moves() Returns a list of possible directions the player can move
			set_available_actions () Appends actions to all_moves
			heal_player() If the room has not be looted heals the player
	"""
	def __init__(self, x, y, player):
		super().__init__(x, y, player, Items.HealingPotionExtreme())

	def intro_text(self):
		"""
		Describes the tile as string

		Output: 
			intro_description <str>
		"""
		if (self.item.is_looted()):

			intro_description = ("A sweet smell from the magic mist in saturates this room.\n")

		else:

			intro_description = ("A magical mist invigorates you and reminds you of your will to live.\n"\
								 "You are healed for {} from the mist.\n".format(self.item.heal_num))

		return intro_description

