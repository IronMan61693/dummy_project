class Item():
	"""
	The base class for all items in the game

	Variables:
		name <str>
		description <str>
		value_copper <int>
		value_silver <int>
		value_gold <int>
		looted <bool>

	Methods:
		is_looted(self): Checks if the item is_looted
		set_looted(self): Sets the item as looted
	"""
	def __init__(self, name, description, value_copper = 0, value_silver = 0, value_gold = 0, looted = False):
		self.name = name
		self.description = description
		self.value_copper = value_copper
		self.value_silver = value_silver
		self.value_gold = value_gold
		self.looted = looted

	def __str__(self):
		"""
		Redefined __str__ to have useful information when call print on the object

		Output:
			<str> <- Object information
		"""
		return "{}\n====\n{}\nValue: {} copper, {} silver, {} gold\n".format(self.name, self.description,\
				 self.value_copper, self.value_silver, self.value_gold)

	def is_looted(self):
		"""
		Checks if the item is_looted

		Output:
			<bool>
		"""
		return self.looted

	def set_looted(self):
		"""
		Sets the item to looted
		"""
		self.looted = True



class Coin(Item):
	"""
	A base class for coins, namely copper silver and gold

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
		coin_amount <int>

	"""
	def __init__(self, coin_name, coin_amount, value_copper = 0, value_silver = 0, value_gold = 0):
		self.coin_amount = coin_amount
		super().__init__(
						 name = coin_name,
						 description = "A round shiny {} coin with {} stamped on the front".format(coin_name, str(self.coin_amount)),
						 )



class CoinPouch(Item):
	"""
	An Item to keep track of Coin

	Variables:
		Inherited from Item:
				name <str>
				description <str>
				value_copper <int>
				value_silver <int>
				value_gold <int>
				looted <bool>
		coins {<str> : <int>}

	Methods:
		add_to_me() Adds the coin_name and new_amt to the pouch
	"""

	def __init__(self):
		self.coins = {"Copper" : 0, "Silver" : 0, "Gold" : 0}

		super().__init__(name = "Coin Pouch",
						 description =  "A pouch containing {} copper pieces, {} silver pieces,"\
						 				" and {} gold.".format(self.coins["Copper"], self.coins["Silver"], self.coins["Gold"]),
						 value_silver = 5)

	def add_to_me(self, coin_name, new_amt):
		"""
		Adds the coin_name and new_amt to the pouch

		Input:
			coin_name <str>
			new_amt <int>
		"""
		self.coins[coin_name] += new_amt
		self.description =  "A pouch containing {} copper pieces, {} silver pieces,"\
						 	" and {} gold.".format(self.coins["Copper"], self.coins["Silver"], self.coins["Gold"])


class Weapon(Item):
	"""
	Extends the Item class, this will be another base class for all specific
	 weapons in the game

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
		quantity_of_die <int>
		damage_die_type <int>
		main_hand <bool>
		off_hand <bool>		
	"""
	def __init__(self, name, description = "Not implemented", quantity_of_die = 1, damage_die_type = 0, value_copper = 0 ,\
				 value_silver = 0, value_gold = 0, main_hand = False, off_hand = False):
		self.quantity_of_die = quantity_of_die
		self.damage_die_type = damage_die_type
		self.main_hand = main_hand
		self.off_hand = off_hand
		super().__init__(name, description, value_copper, value_silver, value_gold)

	def __str__(self):
		"""
		Redefined __str__ to have useful information when call print on the object

		Output:
			<str> 
		"""
		return "{}\n====\n{}\nValue: {} copper, {} silver, {} gold\nDamage: {}d{}".format(self.name, self.description,\
				 self.value_copper, self.value_silver, self.value_gold, self.quantity_of_die, self.damage_die_type)




class Fist(Weapon):
	"""
	Extends the Weapon class

	Variables:
		Inherited from Weapon:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			quantity_of_die <int>
			damage_die_type <int>
			main_hand <bool>
			off_hand <bool>		
	"""
	def __init__(self):
		super().__init__(name = "Fist",
						 description = "Your bruised and battered fist.",
						 value_copper = 1,
						 damage_die_type = 2,
						 main_hand = True)
		self.description += " Does {}d{} damage".format(self.quantity_of_die, self.damage_die_type) 



class ShortSword(Weapon):
	"""
	Extends the Weapon class

	Variables:
		Inherited from Weapon:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			quantity_of_die <int>
			damage_die_type <int>
			main_hand <bool>
			off_hand <bool>		
	"""
	def __init__(self):
		super().__init__(name = "Shord Sword",
						 damage_die_type = 6,
						 description = "A pointy short sword good for sticking enemies.",
						 value_silver = 10,
						 main_hand = True,
						 off_hand = True)
		self.description += " Does {}d{} damage".format(self.quantity_of_die, self.damage_die_type) 



class Dagger(Weapon):
	"""
	Extends the Weapon class

	Variables:
		Inherited from Weapon:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			quantity_of_die <int>
			damage_die_type <int>
			main_hand <bool>
			off_hand <bool>		
	"""
	def __init__(self):
		super().__init__(name = "Dagger",
						 description = "A rust covered dagger, slightly more dangerous than a rock",
						 value_silver = 2,
						 damage_die_type = 4,
						 main_hand = True,
						 off_hand = True)
		self.description += " Does {}d{} damage".format(self.quantity_of_die, self.damage_die_type) 


class Fang(Weapon):
	"""
	Extends the Weapon class

	Variables:
		Inherited from Weapon:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			quantity_of_die <int>
			damage_die_type <int>
			main_hand <bool>
			off_hand <bool>		
	"""
	def __init__(self):
		super().__init__(name = "Fang",
						 damage_die_type = 4,
						 main_hand = True,
						 off_hand = True)

class OgreClub(Weapon):
	"""
	Extends the Weapon class

	Variables:
		Inherited from Weapon:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			quantity_of_die <int>
			damage_die_type <int>
			main_hand <bool>
			off_hand <bool>		
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
			damage <int>
		"""
		super().__init__(name = "Giant Club",
						 damage_die_type = 6,
						 main_hand = True,
						 off_hand = True)