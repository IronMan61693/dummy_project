import random

import  Items
from Inventory import Inventory
from combat import Combat

from Common_Functions import dice_roller


class Player():
	"""
	The player class uses Items class
	 Sets the player to the starting position described in World (0,0)

	Variables:
		name <str>
		player_name <str>
		character_level <int>
		inventory <Inventory>
		hp <int>
		location_x, location_y (<int>,<int>)
		character_class <str>
		strength <int>
		dexterity <int>
		constitution <int>
		intellect <int>
		attributes {<str> : <int>}
		weapon <Weapon>
		dmg_mod <int>

	Methods:
		is_alive() Bool for alive condition determined by hp
		print_inventory() Print statement for player inventory
		view_character() Print statement for information about the player once instantiated
		update_attribute_dictionary() Changes the provided attribute, the key in the dictionary, with the provided value
		set_character_class() Changes the character_class string and all attributes based on the provided string
		get_character_class() Returns the character_class string
		set_character_name() Changes the name string
		get_character_name() Returns the name string
		set_player_name() Changes player_name string
		get_player_name() Returns player_name string
		get_character_level() Returns character_level
		move(dx, dy) Basic move method, dx and dy are change in x and y
		move_north() Calls move dy = -1
		move_south() Calls move dy = 1
		move_east() Calls move dx = 1
		move_west() Calls move dx = -1
		attack() Uses Combat player_attack method
		flee() Allows player to move to random adjacent tile
		 when in combat
		quit() Allow player to exit the game, not used in graphic view
		equip() Prompts the user for which equipment slot would like changed, not use in graphic view
		equip_main_hand_action() Prompts the user for which item would like equipped, not use in graphic view
		do_action() Uses Action class to wrap and mind key press with player methods
	"""
	def __init__(self):
		self.name = "Character"
		self.player_name = "Zorg"
		self.character_level = 1
		self.hp = 100
		self.location_x, self.location_y = (0,0)

		self.inventory = Inventory()
		self.inventory.add_to_pouch("Gold", 15)
		self.inventory.add_to_inventory(Items.Fist(), 1)
		self.inventory.equip_main_hand("Fist")

		self.inventory.add_to_inventory(Items.ShreddedRags(), 1)
		self.inventory.equip_armor("Shredded Rags")

		
		self.character_class = "No Class"
		self.strength = 10
		self.dexterity = 10
		self.constitution = 10
		self.intellect = 10
		self.attributes = {"Strength: " : self.strength, "Dexterity: " : self.dexterity,
							"Constitution: " : self.constitution, "Intellect: " : self.intellect}


		self.weapon = self.inventory.get_main_hand_equipped()
		self.dmg_mod = 4

		self.armor = self.inventory.get_armor_equipped()
		self.ArmorClass = self.armor.AC

	def hit_check(self):
		"""
		Returns the difference between the bonus of the weapon to hit and the penalty from the armor

		Output:
			<int>
		"""
		return (self.weapon.to_hit - self.armor.to_hit_mod)



	def is_alive(self):
		"""
		Bool for alive condition determined by hp
		
		Output:
			<bool>
		"""
		return self.hp > 0



	def print_inventory(self):
		"""
		Uses inventory print_inventory method to print player inventory
		"""
		self.inventory.print_inventory()


	def view_character(self):
		"""
		Print statement for information about the instance of player Class
		"""
		print("Player: {}".format(self.player_name))
		print("Character: {}".format(self.name))
		print("Level: {}".format(self.character_level))
		print("You have {} HP remaining".format(self.hp))
		print(self.character_class)
		for key, value in self.attributes.items():
			print(key,  str(value))



	def update_attribute_dictionary(self, attribute, new_value):
		"""
		Changes the provided attribute, the key in the dictionary, with the provided value

		Input:
			attribute <str>
			new_value <int>
		"""
		if attribute in self.attributes.keys():
			self.attributes[attribute] = new_value



	def set_character_class(self, class_name):
		"""
		Changes the player Class instanced attributes (Strength Dexterity Constitution Intellect)
		 Depending on the class_name input.

		Input:
			class_name <str>
		"""
		if (class_name == "Barbarian"):
			self.character_class = class_name
			self.strength = 14
			self.dexterity = 8
			self.constitution = 12
			self.intellect = 6

			self.inventory.add_to_inventory(Items.BattleAxe(), 1)
			self.inventory.equip_main_hand("Battle Axe")

		elif (class_name == "Knight"):
			self.character_class = class_name
			self.strength = 12
			self.dexterity = 8
			self.constitution = 12
			self.intellect = 8

			self.inventory.add_to_inventory(Items.LongSword(), 1)
			self.inventory.equip_main_hand("Long Sword")

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

			self.inventory.add_to_inventory(Items.Dagger(), 1)
			self.inventory.equip_main_hand("Dagger")
	
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
		"""
		Returns the character_class string

		Output:
			character_class <str>
		"""
		return self.character_class




	def set_character_name(self, char_name):
		"""
		Changes the character_name string to the input string

		Input:
			char_name <str>
		"""
		self.name = char_name



	def get_character_name(self):
		"""
		Returns name string

		Output:
			name <str>
		"""
		return self.name



	def set_player_name(self, play_name):
		"""
		Changes the  player_name string to the input string

		Input:
			play_name <str>
		"""
		self.player_name = play_name



	def get_player_name(self):
		"""
		Returns player_name string

		Output:
			player_name <str>
		"""
		return self.player_name



	def get_character_level(self):
		"""
		Returns character_level int

		Output:
			character_level <int>
		"""
		return self.character_level



	def move(self, dx, dy):
		"""
		basic move method, dx and dy are change in x and y

		Input:
			dx <int>
			dy <int>
		"""
		self.location_x += dx
		self.location_y += dy


	def move_north(self):
		"""
		use move() method to move character decreasing in dy
		"""
		self.move(dx = 0, dy = -1)



	def move_south(self):
		"""
		use move() method to move character increasing in dy
		"""
		self.move(dx = 0, dy = 1)



	def move_east(self):
		"""
		use move() method to move character increasing in dx
		"""
		self.move(dx = 1, dy = 0)



	def move_west(self):
		"""
		use move() method to move character decreasing in dx
		"""
		self.move(dx = -1, dy = 0)



	def attack(self, combatClass):
		"""
		Uses Combat player_attack method

		Input:
			combatClass <Combat>
		"""
		combatClass.player_attack()

	def flee(self, tile):
		"""
		Allows player to move to random adjacent tile in combat

		Input:
			tile <MapTile>
		"""
		available_moves = tile.adjacent_moves()
		random_direction = random.randint(0,len(available_moves) -1)
		self.do_action(available_moves[random_direction])



	def quit(self):
		"""
		Allows player to exit the game
		"""
		print("You have decided to leave the adventure early. See you next time!")
		self.hp = 0



	def equip(self):
		"""
		Prompts the user for which equipment slot would like changed, not use in graphic view
		"""
		equipment_choice = print("Select which piece of equipment you would like to change.\n"
								 "1 For main hand, 2 For off hand, 3 for armor, 4 for ring and 5 for amulet.")
		if equipment_choice == 1:
			self.equip_main_hand_action()



	def equip_main_hand_action(self):
		"""
		Prompts the user for which main weapon would like changed, not use in graphic view
		"""
		print("Choose the item you would like to equip from the following items in your inventory.")
		for weapon in self.inventory.get_main_hand_options():
			print(weapon)
		weapon_choice = input("Type the name of the weapon you would like to equip.")
		for weapon in self.inventory.get_main_hand_options():
			if weapon_choice == weapon.name:
				self.inventory.equip_main_hand(weapon)



	def do_action(self, action, **kwargs):
		"""
		Allows Action to implement Player methods

		Input:
			action <Action>
			kwargs <char>
		"""
		action_method = getattr(self, action.method.__name__)

		# Verifies valid input
		if action_method:
			action_method(**kwargs)



