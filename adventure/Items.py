from Common_Functions import dice_roller

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














class HealingPotion(Item):
	"""
	A base class for healing potions, weak 1d6+4, medium 1d8+5, strong 1d10+6, superior 1d12+7, extreme 1d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
		heal_num <int>
	"""
	def __init__(self, name, heal_num, description = "No description health pot", value_copper = 0, value_silver = 0,\
				 value_gold = 0):
		self.heal_num = heal_num
		super().__init__(name, description, value_copper, value_silver, value_gold)



class HealingPotionWeak(HealingPotion):
	"""
	A Healing Potion, weak 2d6+4, medium 2d8+5, strong 2d10+6, superior 2d12+7, extreme 2d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			heal_num <int>
	"""
	def __init__(self):
		super().__init__(name = "HealingPotionWeak", heal_num = dice_roller(2,6,4))



class HealingPotionMedium(HealingPotion):
	"""
	A Healing Potion, weak 2d6+4, medium 2d8+5, strong 2d10+6, superior 2d12+7, extreme 2d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			heal_num <int>
	"""
	def __init__(self):
		super().__init__(name = "HealingPotionMedium", heal_num = dice_roller(2,8,5))



class HealingPotionStrong(HealingPotion):
	"""
	A Healing Potion, weak 2d6+4, medium 2d8+5, strong 2d10+6, superior 2d12+7, extreme 2d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			heal_num <int>
	"""
	def __init__(self):
		super().__init__(name = "HealingPotionStrong", heal_num = dice_roller(2,10,6))



class HealingPotionSuperior(HealingPotion):
	"""
	A Healing Potion, weak 2d6+4, medium 2d8+5, strong 2d10+6, superior 2d12+7, extreme 2d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			heal_num <int>
	"""
	def __init__(self):
		super().__init__(name = "HealingPotionSuperior", heal_num = dice_roller(2,12,7))



class HealingPotionExtreme(HealingPotion):
	"""
	A Healing Potion, weak 2d6+4, medium 2d8+5, strong 2d10+6, superior 2d12+7, extreme 2d20+8

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			heal_num <int>
	"""
	def __init__(self):
		super().__init__(name = "HealingPotionExtreme", heal_num = dice_roller(2,20,8))
















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
		super().__init__(name = coin_name,
						 description = "A round shiny {} coin with {} stamped on the front".format(coin_name, str(self.coin_amount)),
						 )



class Gold(Coin):
	"""
	Extends the Coin Class

	Variables:
		Inherited from Coin:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
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
		to_hit <int>	
	"""
	def __init__(self, name, description = "Not implemented weapon", quantity_of_die = 1, damage_die_type = 0, 
				 value_copper = 0 ,value_silver = 0, value_gold = 0, main_hand = False, off_hand = False, to_hit = 0):
		self.quantity_of_die = quantity_of_die
		self.damage_die_type = damage_die_type
		self.main_hand = main_hand
		self.off_hand = off_hand
		self.to_hit = to_hit
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Fist",
						 description = "Your bruised and battered fist.",
						 value_copper = 1,
						 damage_die_type = 2,
						 to_hit = 4,
						 main_hand = True)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 



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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Shord Sword",
						 quantity_of_die = 2,
						 damage_die_type = 6,
						 description = "A pointy short sword good for sticking enemies.",
						 value_silver = 10,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 9)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 



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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Dagger",
						 description = "A rust covered dagger, slightly more dangerous than a rock",
						 value_silver = 2,
						 quantity_of_die = 2,
						 damage_die_type = 4,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 10)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 



class QuarterStaff(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Quarter Staff",
						 description = "A solid chunk of wood with iron caps on either end",
						 value_silver = 7,
						 quantity_of_die = 2,
						 damage_die_type = 8,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 8)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 




class BattleAxe(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Battle Axe",
						 quantity_of_die = 2,
						 damage_die_type = 12,
						 description = "A big and burly axe.",
						 value_silver = 56,
						 main_hand = True,
						 to_hit = 6)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 




class LongSword(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Long Sword",
						 quantity_of_die = 2,
						 damage_die_type = 10,
						 description = "A typical longsword as seen accompanying knights.",
						 value_silver = 35,
						 main_hand = True,
						 to_hit = 7)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 





class MoonSword(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Moon Sword",
						 quantity_of_die = 5,
						 damage_die_type = 12,
						 description = "An amazing sword glowing with a purple aura.",
						 value_gold = 1000,
						 main_hand = True,
						 to_hit = 12)
		self.description += " Does {}d{} damage and a +{} to hit.".format(self.quantity_of_die, self.damage_die_type, self.to_hit) 







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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Fang",
						 damage_die_type = 6,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 6)



class MassiveClub(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Massive Club",
						 quantity_of_die = 2,
						 damage_die_type = 8,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 8)



class AssassinDagger(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Assassin's Dagger",
						 quantity_of_die = 4,
						 damage_die_type = 8,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 8)



class DeathSword(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Long Sword",
						 quantity_of_die = 7,
						 damage_die_type = 6,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 14)




class WizardStaff(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Wizard Fireball",
						 quantity_of_die = 6,
						 damage_die_type = 6,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 8)



class PoisonBreath(Weapon):
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
			to_hit <int>		
	"""
	def __init__(self):
		super().__init__(name = "Poison Breath",
						 quantity_of_die = 4,
						 damage_die_type = 10,
						 main_hand = True,
						 off_hand = True,
						 to_hit = 16)
















class Armor(Item):
	"""
	Extends the Item class, this will be another base class for all specific
	 armor in the game

	Variables:
		Inherited from Item:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
		armor <bool>
		to_hit_mod <int>
			
	"""
	def __init__(self, armor_name, description = "Not implemented armor", value_copper = 0, value_silver = 0,\
	 			 value_gold = 0, AC = 0, to_hit_mod = 0):
		self.AC = AC
		self.to_hit_mod = to_hit_mod
		super().__init__(armor_name, description = description)
		self.description += " Provides {} armor and detracts from ability to hit by {}.".format(self.AC, self.to_hit_mod)



class ShreddedRags(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Shredded Rags",
						 description = "Rags terribly shredded and barely hanging to your form",
						 value_copper = 6,
						 AC = 6,
						 to_hit_mod = 1)



class PaddedCloth(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Padded Clothes",
						 description = "Consists of quilted layers of cloth.",
						 value_silver = 1,
						 AC = 11,
						 to_hit_mod = 0)



class StuddedLeather(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Studded Leather",
						 description = "Nice leather armor with metal studs throughout.",
						 value_silver = 8,
						 AC = 13,
						 to_hit_mod = 1)




class ChainShirt(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Chain Shirt",
						 description = "Interlocking metal rings covering the wearer's upper body.",
						 value_silver = 15,
						 AC = 15,
						 to_hit_mod = 3)



class RingMail(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Ring Mail",
						 description = "Leather armor with strong metal woven throughout.",
						 value_gold = 1,
						 AC = 17,
						 to_hit_mod = 4)




class FullPlate(Armor):
	"""
	Extends the Armor class

	Variables:
		Inherited from Armor:
			name <str>
			description <str>
			value_copper <int>
			value_silver <int>
			value_gold <int>
			looted <bool>
			armor <bool>
			to_hit_mod <int>
	"""
	def __init__(self):
		super().__init__(armor_name = "Full Plate",
						 description = "Shaped, interlocking metal plates to cover the entire body. .",
						 value_gold = 1,
						 AC = 19,
						 to_hit_mod = 5)

