import Items

class Inventory():
	def __init__(self):
		self.inventoryDictionary = {}
		self.equippedMainHand = None
		self.equippedOffHand = None
		self.equippedArmor = None
		self.equippedRing = None
		self.equippedAmulet = None
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
		for key in self.inventoryDictionary:
			if key.name == weapon:
				self.equippedMainHand = key

	def get_main_hand_equipped(self):
		return self.equippedMainHand

	def get_all_equipped(self):
		# order main_hand, off_hand, armor, ring, amulet
		return (self.get_main_hand_equipped(), None, None, None, None)

	def get_inventory_dict(self):

		return self.inventoryDictionary

	def get_main_hand_options(self):
		# Use this in order to seperate Items by types
		# for weap in self.inventory:
		# 	if isinstance(weap,  Items.Weapon):
		# 		if weap.damage > max_dmg:
		# 			max_dmg = weap.damage
		# 			best_weapon = weap
		# isinstance(weap,  Items.Weapon)
		options = []
		for weap in self.inventoryDictionary:
			if isinstance(weap, Items.Weapon):
				if weap.main_hand:
					options.append(weap.name)

		return options

	def print_inventory(self):

		for item, amount in self.inventoryDictionary.items():
			print ("Item: " + item.name + " Quantity: " + str(amount))
			print (item.description + "\n")

		print("Currently equipped: ")
		print("Main Hand: " + self.equippedMainHand.name)


