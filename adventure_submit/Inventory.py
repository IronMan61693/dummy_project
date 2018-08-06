import Items

class Inventory():
	"""
	A class for maintaining and interacting with the player's inventory

	Variables:
		inventoryDictionary {<Item> : <int>}
		equippedMainHand <Weapon>
		coin_pouch <CoinPouch>

	Methods:
		add_to_pouch() Adds named coin and quantity to coin pouch
		add_to_inventory() Adds Item object to inventory with quantity as value, 
		 if Item already in inventory updates quantity
		equip_main_hand() Changes equippedMainHand variable
		get_main_hand_equipped() Returns equippedMainHand variable
		get_all_equipped() Returns tuple for all future equippment slots
		get_inventory_dict() Returns inventoryDictionary
		get_main_hand_options() Return list for all weapons with True main_hand
		print_inventory() A print statement for the inventory
	"""
	def __init__(self):
		self.inventoryDictionary = {}
		self.equippedMainHand = None
		# self.equippedOffHand = None
		# self.equippedArmor = None
		# self.equippedRing = None
		# self.equippedAmulet = None
		self.coin_pouch = Items.CoinPouch()

		self.add_to_inventory(self.coin_pouch, 1)

	def add_to_pouch(self, coin_name, coin_amount):
		"""
		For the instance of CoinPouch called my_coin_pouch calls
		 method add_to_me with the variables coi_name and coin_value

		Input:
			coin_name <str>
			coin_value <int>
		"""
		self.coin_pouch.add_to_me(coin_name, coin_amount)


	def add_to_inventory(self, item, quantity):
		"""
		Adds Item object to inventory with quantity as value, 
		 if Item already in inventory updates quantity

		Input:
			item <Item>
			quantity <int>
		"""
		increaseQuantity = None
		addToDict = True
		for key in self.inventoryDictionary:
			if key.name == item.name:
				addToDict = False
				increaseQuantity = key
				break
				

			else:
				addToDict = True
				

		if addToDict:
			self.inventoryDictionary[item] = quantity
		else:
			self.inventoryDictionary[increaseQuantity] += quantity


	def equip_main_hand(self, weapon):
		"""
		Changes the equippedMainHand variable, returns true if Item was in inventory and 
		 equipped and false if not

		Input:
			weapon <Weapon>

		Output:
			<bool>
		"""
		for key in self.inventoryDictionary:
			if key.name == weapon:
				self.equippedMainHand = key
				return True
		return False

	def get_main_hand_equipped(self):
		return self.equippedMainHand

	def get_all_equipped(self):
		"""
		Returns equippedMainHand variable
		 order main_hand, off_hand, armor, ring, amulet

		Output:
			(<Weapon>, <bool>, <bool>, <bool>, <bool>)
		"""
		
		return (self.get_main_hand_equipped(), None, None, None, None)

	def get_inventory_dict(self):
		"""
		Returns inventoryDictionary variable

		Output:
			{<Item> : <int>}
		"""
		return self.inventoryDictionary

	def get_main_hand_options(self):
		"""
		Return list for all weapons with True main_hand

		Output:
			options[<Weapon>]
		"""
		options = []
		for weap in self.inventoryDictionary:
			if isinstance(weap, Items.Weapon):
				if weap.main_hand:
					options.append(weap.name)

		return options

	def print_inventory(self):
		"""
		A print statement for the inventory
		"""
		for item, amount in self.inventoryDictionary.items():
			print ("Item: " + item.name + " Quantity: " + str(amount))
			print (item.description + "\n")

		print("Currently equipped: ")
		print("Main Hand: " + self.equippedMainHand.name)


