import Items
from Common_Functions import dice_roller

class Enemy:
	"""
	Base class for Enemies

	Variables:
		name <str>
		hp <int>
		weapon <Weapon>
		dmg_mod <int>

	Methods:
		is_alive(self) Method to determine if enemy is alive, true or false 
		 base on hp
	"""
	def __init__(self, name, hp, weapon, dmg_mod, armor):
		
		self.name = name
		self.hp = hp 
		self.weapon = weapon 
		self.dmg_mod = dmg_mod
		self.armor = armor
		self.ArmorClass = self.armor.AC
	
	def is_alive(self):
		"""
		Return true if hp is above 0 return false if hp of enemy <= 0

		Output:
			<bool>
		"""
		return self.hp > 0

	def hit_check(self):
		"""
		Returns the difference between the bonus of the weapon to hit and the penalty from the armor

		Output:
			<int>
		"""
		return (self.weapon.to_hit - self.armor.to_hit_mod)



class GiantSpider(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Giant Spider", hp=dice_roller(2,8,2), weapon = Items.Fang(), dmg_mod = 1, armor = Items.StuddedLeather())



class Ogre(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Ogre", hp=dice_roller(2,10,18), weapon = Items.MassiveClub(), dmg_mod = 4, armor = Items.PaddedCloth())



class Bandit(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Bandit", hp=dice_roller(2,8,2), weapon = Items.ShortSword(), dmg_mod = 1, armor = Items.PaddedCloth())


class Valkyrie(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Valkyrie", hp=dice_roller(2,12,4), weapon = Items.BattleAxe(), dmg_mod = 3, armor = Items.PaddedCloth())

class Assassin(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Assassin", hp=dice_roller(3,8,8), weapon = Items.Dagger(), dmg_mod = 8, armor = Items.StuddedLeather())

class DeathKnight(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Death Knight", hp=dice_roller(4,10,20), weapon = Items.LongSword(), dmg_mod = 8, armor = Items.FullPlate())

class Giant(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Giant", hp=dice_roller(3,20,25), weapon = Items.MassiveClub(), dmg_mod = 5, armor = Items.ChainShirt())


class GreenDragon(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Green Dragon", hp=dice_roller(5,12,15), weapon = Items.PoisonBreath(), dmg_mod = 10, armor = Items.FullPlate())



class Wizard(Enemy):
	"""
	Subclass of Enemy

	Variables:
		Inherited from Enemy:
			name <str>
			hp <int>
			weapon <Weapon>
			dmg_mod <int>
	"""
	def __init__(self):
		super().__init__(name="Wizard", hp=dice_roller(2,8,5), weapon = Items.WizardStaff(), dmg_mod = 15, armor = Items.PaddedCloth())

"""

Bandit *8 G Spider * 6 Valkyrie * 4  Ogre * 2 Assassin * 1
DeathKnight 0  Giant 0 GreenDragon 0  Wizard 0
"""