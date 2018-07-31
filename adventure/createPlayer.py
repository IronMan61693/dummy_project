import random

import  Items

from Common_Functions import dice_roller


class Player():
	"""
	The player class uses Items class
	 Sets the player to the starting position described in World

	Variables:
		inventory [<Items>]
		hp <int>
		location_x <int>
		location_y <int>
		victory <bool>

	Methods:
		is_alive() bool for alive condition determined by hp
		print_inventory() print statement for player inventory
		move(dx, dy) basic move method, dx and dy are change in x and y
		move_north() calls move dy = -1
		move_south() calls move dy = 1
		move_east() calls move dx = 1
		move_west() calls move dx = -1
		attack(enemy) finds the best weapon in inventory
		 and decrements enemy hp by the weapon.damage
		flee(tile) Allows player to move to random adjacent tile
		 when in combat
		do_action(action, kwargs) uses Action class to run
		 the action's method  , Items.Fist()

	"""
	def __init__(self):
		self.character_name = "Character"
		self.player_name = "Zorg"
		self.character_level = 1
		self.my_coin_pouch =  Items.CoinPouch()
		self.my_coin_pouch.add_to_me("Gold", 15)
		self.inventory = [self.my_coin_pouch,  Items.Fist()]
		self.hp = 100
		self.location_x, self.location_y =   (0,0)
		self.victory = False
		self.character_class = "No Class"
		self.strength = 10
		self.dexterity = 10
		self.constitution = 10
		self.intellect = 10
		self.attributes = {"Strength: " : self.strength, "Dexterity: " : self.dexterity,
							"Constitution: " : self.constitution, "Intellect: " : self.intellect}





	def add_to_pouch(self, coin_name, coin_amount):
		"""
		For the instance of CoinPouch called my_coin_pouch calls
		 method add_to_me with the variables coi_name and coin_value

		Input:
			coin_name <str>
			coin_value <int>
		"""
		self.my_coin_pouch.add_to_me(coin_name, coin_amount)
		


	def is_alive(self):
		"""
		bool for alive condition determined by hp
		
		Output <bool>
		"""
		return self.hp > 0



	def print_inventory(self):
		"""
		print statement for player inventory

		Output:
			print statement
		"""
		for item in self.inventory:
			print(item, '\n')


	def view_character(self):
		"""
		print statement for information about the instance of player Class

		Output:
			print statement
		"""
		print("Player: {}".format(self.player_name))
		print("Character: {}".format(self.character_name))
		print("Level: {}".format(self.character_level))
		# print("You have beaten {} tiles!".format(World.how_many_tile()))
		print("You have {} HP remaining".format(self.hp))
		print(self.character_class)
		for key, value in self.attributes.items():
			print(key,  str(value))



	def update_attribute_dictionary(self, attribute, new_value):
		if attribute in self.attributes.keys():
			self.attributes[attribute] = new_value



	def set_character_class(self, class_name):
		"""
		Changes the player Class instanced attributes (Strength Dexterity Constitution Intellect)
		 Depending on the class_name input.

		Input:
			class_name <str>

		Output:
			Modifies player instance
		"""
		if (class_name == "Barbarian"):
			self.character_class = class_name
			self.strength = 14
			self.dexterity = 8
			self.constitution = 12
			self.intellect = 6

		elif (class_name == "Knight"):
			self.character_class = class_name
			self.strength = 12
			self.dexterity = 8
			self.constitution = 12
			self.intellect = 8

		elif (class_name == "Nerd"):
			self.character_class = class_name
			self.strength = 8
			self.dexterity = 8
			self.constitution = 8
			self.intellect = 16

		elif (class_name == "Rogue"):
			self.character_class = class_name
			self.strength = 6
			self.dexterity = 14
			self.constitution = 8
			self.intellect = 12

		else:
			self.character_class = "No Class"
			self.strength = 10
			self.dexterity = 10
			self.constitution = 10
			self.intellect = 10

		self.update_attribute_dictionary("Strength: ", self.strength)
		self.update_attribute_dictionary("Dexterity: ", self.dexterity)
		self.update_attribute_dictionary("Constitution: ", self.constitution)
		self.update_attribute_dictionary("Intellect: ", self.intellect)




	def get_character_class(self):
		return self.character_class




	def set_character_name(self, char_name):
		"""
		Changes the player Class instanced variable character_name to the input string

		Input:
			char_name <str>

		Output:
			Modifies player instance
		"""
		self.character_name = char_name



	def get_character_name(self):
		return self.character_name



	def set_player_name(self, play_name):
		"""
		Changes the player Class instanced variable player_name to the input string

		Input:
			play_name <str>

		Output:
			Modifies player instance
		"""
		self.player_name = play_name



	def get_player_name(self):
		return self.player_name



	def get_character_level(self):
		return self.character_level




	def move(self, dx, dy):
		"""
		basic move method, dx and dy are change in x and y

		Input:
			dx <int>
			dy <int>

		Output:
			print statement for tile entered
		"""
		self.location_x += dx
		self.location_y += dy
		# if not  World.tile_exists(self.location_x, self.location_y):
		# 	World.generate_world(self.location_x, self.location_y)
		# print(World.tile_exists(self.location_x, self.location_y).intro_text())



	def move_north(self):
		"""
		use move() method to move character decreasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = -1)



	def move_south(self):
		"""
		use move() method to move character increasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = 1)



	def move_east(self):
		"""
		use move() method to move character increasing in dx

		Output:
			move(0, -1)
		"""
		self.move(dx = 1, dy = 0)



	def move_west(self):
		"""
		use move() method to move character decreasing in dx

		Output:
			move(0, -1)
		"""
		self.move(dx = -1, dy = 0)



	def attack(self, enemy):
		"""
		Uses the weapon with the highest damage in the
		 player inventory to decrement hp of enemy

		Input:
			enemy <Enemy>

		Output:
			modifies enemy instance
			print statement
		"""
		best_weapon = None
		max_dmg = 0

		# Finds the most damage weapon in inventory
		for weap in self.inventory:
			if isinstance(weap,  Items.Weapon):
				if weap.damage > max_dmg:
					max_dmg = weap.damage
					best_weapon = weap

		print("You used your {} against the {}!".format(best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage

		if not enemy.is_alive():
			print("You killed the {}!".format(enemy.name))

		else:
			print("The {}'s HP is now {}.".format(enemy.name, enemy.hp))



	def flee(self, tile):
		"""
		Allows player to move to random adjacent tile in combat

		Input:
			tile <MapTile>
		"""
		available_moves = tile.adjacent_moves()
		r = random.randint(0,len(available_moves) -1)
		self.do_action(available_moves[r])



	def quit(self):
		"""
		Allows player to exit the game
		"""
		print("You have decided to leave the adventure early. See you next time!")
		self.hp = 0




	def do_action(self, action, **kwargs):
		"""
		Allows Action to implement Player methods

		Input:
			action <Action>
			kwargs <char> <- keyboard input
		"""
		action_method = getattr(self, action.method.__name__)

		# Verifies valid input
		if action_method:
			action_method(**kwargs)