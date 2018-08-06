from createPlayer import Player

class Action():
	"""
	A way to bind the keys to the methods of the player class
	 A base class for further actions
	
	Variables:
		method <method> in Player class
		name <string>
		hotkey <char> 
		moved <bool
		**kwargs read user input

	"""
	def __init__(self, method, name, hotkey, moved = False, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.moved = moved
		self.kwargs = kwargs

	def __str__(self):
		"""
		Provides useful information if print called on this object
		"""
		return "{}: {}".format(self.hotkey, self.name)



class MoveNorth(Action):
	"""
	Subclass of Action, binds w to method move_north from Player class
	 Fills in specific information for Action baseclass init
	 See <Action> for further information
	"""
	def __init__(self):
		super().__init__(method = Player.move_north, name = "Move up", hotkey = 'w', moved = True)



class MoveSouth(Action):
	"""
	Subclass of Action, binds s to method move_south from Player class
	 Fills in specific information for Action baseclass init
	 See <Action> for further information
	"""
	def __init__(self):
		super().__init__(method = Player.move_south, name = "Move down", hotkey = 's', moved = True)



class MoveEast(Action):
	"""
	Subclass of Action, binds d to method move_east from Player class
	 Fills in specific information for Action baseclass init
	 See <Action> for further information
	"""
	def __init__(self):
		super().__init__(method = Player.move_east, name = "Move right", hotkey = 'd', moved = True)



class MoveWest(Action):
	"""
	Subclass of Action, binds a to method move_west from Player class
	 Fills in specific information for Action baseclass init
	 See <Action> for further information
	"""
	def __init__(self):
		super().__init__(method = Player.move_west, name = "Move left", hotkey = 'a', moved = True)



class ViewInventory(Action):
	"""
	Subclass of Action, binds i to method print_inventory from Player class
	 fills in specific info for Action baseclass
	"""
	def __init__(self):
		super().__init__(method = Player.print_inventory, name = "View inventory", hotkey = 'i')



class ViewCharacter(Action):
	"""
	Subclass of Action, binds i to method view_character from Player class
	 fills in specific info for Action baseclass
	"""
	def __init__(self):
		super().__init__(method = Player.view_character, name = "View character", hotkey = 'c')



class Attack(Action):
	"""
	Subclass of Action, binds a to method attack from Player class
	 fills in specific info for Action baseclass
	"""
	def __init__(self, combatClass):
		super().__init__(method = Player.attack, name = "Attack", hotkey = 'k', combatClass = combatClass)



class Flee(Action):
	"""
	Subclass of Action, binds f to method flee from Player class
	 fills in specific info for Action baseclass
	"""
	def __init__(self, tile):
		super().__init__(method = Player.flee, name = "Flee", hotkey = 'f', tile = tile, moved = True)


class Equip(Action):
	"""
	Subclass of Action, binds o to method equip from Player class
	 fills in specific info for Action baseclass
	"""
	def __init__(self):
		super().__init__(method = Player.equip, name = "Equip", hotkey = 'o')



# class Quit(Action):
# 	"""
# 	Subclass of Action, binds q to method quit from Player class
# 	"""
# 	def __init__(self):
# 		super().__init__(method = Player.quit, name = "Quit", hotkey = 'q')