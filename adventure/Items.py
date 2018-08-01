class Item():
	"""
	The base class for all items in the game

	Variables:
		name <str>
		description <str>
		value <int>

	Methods:
		__init__(self, name, description, value): Initializes the base class
		__str__(self): returns a string with the information of the item
		is_looted(self): Checks if the item is_looted
		set_looted(self): Sets the item as looted
	"""
	def __init__(self, name, description, value_copper = 0, value_silver = 0, value_gold = 0, looted = False):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
		"""
		self.name = name
		self.description = description
		self.value_copper = value_copper
		self.value_silver = value_silver
		self.value_gold = value_gold
		self.looted = looted

	def __str__(self):
		"""
		Redefined __str__ to have useful information when call print on the object

		Input:
			None

		Output:
			<str> <- Object information
		"""
		return "{}\n====\n{}\nValue: {} copper, {} silver, {} gold\n".format(self.name, self.description,\
				 self.value_copper, self.value_silver, self.value_gold)

	def is_looted(self):
		"""
		Checks if the item is_looted
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
		amt <int>
		name <str>
		description <str>
		value <int>

	Methods:
		__init__(self, amt): Initializes as subclass of Item and add amt variable
	"""
	def __init__(self, coin_name, coin_amount, value_copper = 0, value_silver = 0, value_gold = 0):
		"""
		Input: 
			amt <int>
		"""

		self.coin_amount = coin_amount
		super().__init__(
						 name = coin_name,
						 description = "A round shiny {} coin with {} stamped on the front".format(coin_name, str(self.coin_amount)),
						 )



class Gold(Coin):
	"""
	Extends the Item class specifically to gold, as a means of currency in the game
	 This class holds the value of gold pieces as amt
	 Is a subclass of superclass Item

	Variables:
		amt <int>
		name <str>
		description <str>
		value <int>

	Methods:
		__init__(self, amt): Initializes as subclass of Item and add amt variable
	"""
	def __init__(self, amount):
		"""
		Input: 
			amount <int>
		"""

		self.amount = amount
		super().__init__(coin_name = "Gold",
						 coin_amount = self.amount,
						 value_gold = self.amount)

class CoinPouch(Item):
	"""
	TBD Change all values to reflect copper silver and gold
	"""

	def __init__(self):
		self.coins = {"Copper" : 0, "Silver" : 0, "Gold" : 0}

		super().__init__(name = "Coin Pouch",
						 description =  "A pouch containing {} copper pieces, {} silver pieces,"\
						 				" and {} gold.".format(self.coins["Copper"], self.coins["Silver"], self.coins["Gold"]),
						 value_silver = 5)

	def add_to_me(self, coin_name, new_amt):
		self.coins[coin_name] += new_amt
		self.description =  "A pouch containing {} copper pieces, {} silver pieces,"\
						 	" and {} gold.".format(self.coins["Copper"], self.coins["Silver"], self.coins["Gold"])
		# TBD have a value



class Weapon(Item):
	"""
	Extends the Item class, this will be another base class for all specific
	 weapons in the game

	Variables:
		name <str>
		description <str>
		value <int>
		damage <int>

	Methods:
		__init__(self, name, description, value, damage) calls Item init, adds damage variable
		__str__(self): returns a string with the information of the weapon
	"""
	def __init__(self, name, description, damage, value_copper = 0 , value_silver = 0, value_gold = 0, main_hand = False, \
				 off_hand = False):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
			damage <int>
		"""
		self.damage = damage
		self.main_hand = main_hand
		self.off_hand = off_hand
		super().__init__(name, description, value_copper, value_silver, value_gold)

	def __str__(self):
		"""
		Redefined __str__ to have useful information when call print on the object

		Output:
			<str> <- Object information
		"""
		return "{}\n====\n{}\nValue: {} copper, {} silver, {} gold\nDamage: {}".format(self.name, self.description,\
				 self.value_copper, self.value_silver, self.value_gold, self.damage)




class Fist(Weapon):
	"""
	A specific weapon Fist subclass of Weapon

	Variables:
		name <str>
		description <str>
		value <int>
		damage <int>

	Methods:
		__init__(self): Initializes as subclass of Weapon
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
			damage <int>
		"""
		super().__init__(name = "Fist",
						 description = "Your bruised and battered fist.",
						 value_copper = 1,
						 damage = 3,
						 main_hand = True)



class Rock(Weapon):
	"""
	A specific weapon Rock subclass of Weapon

	Variables:
		name <str>
		description <str>
		value <int>
		damage <int>

	Methods:
		__init__(self): Initializes as subclass of Weapon
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
			damage <int>
		"""
		super().__init__(name = "Rock",
						 description = "A fist-sized rock, suitable for bludgeoning heads",
						 value_copper = 5,
						 damage = 5,
						 main_hand = True)



class Dagger(Weapon):
	"""
	A specific weapon Dagger subclass of Weapon

	Variables:
		name <str>
		description <str>
		value <int>
		damage <int>

	Methods:
		__init__(self): Initializes as subclass of Weapon
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
			damage <int>
		"""
		super().__init__(name = "Dagger",
						 description = "A rust covered dagger, slightly more dangerous than a rock",
						 value_silver = 10,
						 damage = 10,
						 main_hand = True,
						 off_hand = True)
