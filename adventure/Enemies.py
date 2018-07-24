class Enemy:
	"""
	Base class for Enemies

	Variables:
		name <str>
		hp <int>
		damage <int>
		difficulty <int>

	Methods:
		__init__(self,name,hp,damage) Initializes base enemy class
		is_alive(self) Method to determine if enemy is alive, true or false 
		 base on hp
	"""
	def __init__(self, name, hp, damage):
		"""
		Initializes the Enemy base Class

		Input: 
			name <str>
			hp <int>
			damage <int>

		Output: 
			None
		"""
		self.name = name
		self.hp = hp 
		self.damage = damage 
	
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
		name <str>
		hp <int>
		damage <int>

	Methods:
		__init__(self) calls Enemy init method with specific information 
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			hp <int>
			damage <int>
		"""
		super().__init__(name="Giant Spider", hp=10, damage=2)



class Ogre(Enemy):
	"""
	Subclass of Enemy

	Variables:
		name <str>
		hp <int>
		damage <int>

	Methods:
		__init__(self) calls Enemy init method with specific information 
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			hp <int>
			damage <int>
		"""
		super().__init__(name="Ogre", hp=30, damage=15)