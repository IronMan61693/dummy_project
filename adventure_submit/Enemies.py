import Items

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
	def __init__(self, name, hp, weapon, dmg_mod):
		
		self.name = name
		self.hp = hp 
		self.weapon = weapon 
		self.dmg_mod = dmg_mod
	
	def is_alive(self):
		"""
		Return true if hp is above 0 return false if hp of enemy <= 0

		Output:
			<bool>
		"""
		return self.hp > 0



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
		super().__init__(name="Giant Spider", hp=10, weapon = Items.Fang(), dmg_mod = 2)



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
		super().__init__(name="Ogre", hp=30, weapon = Items.OgreClub(), dmg_mod = 4)