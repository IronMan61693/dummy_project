from Common_Functions import dice_roller

class Combat():
	"""
	A class which holds the two combatants, facilitates their attack actions, and maintains information about them

	Variables:
		player <Player>
		enemy <Enemy>
		attacker <Player/Enemy>
		defender <Player/Enemy>
		hit_string <str>
		enemy_combat_string <str>
		player_combat_string <str>
		damage <int>

	Methods:
		player_attack() Uses attack with the player as the attacker and sets the player_combat_string
		enemy_attack() Uses attack with the enemy as the attacker and sets the enemy_combat_string
		attack() Updates attacker, changes hit_string, uses attack_damage to determine damage done 
		 and lowers defender hp appropriately
		attack_damage() Uses dice_roller common function to determine damage
		combat_description() Formats the information of the attacks in a string
	"""
	def __init__(self, player, enemy):
		self.player = player
		self.enemy = enemy

		self.attacker = self.enemy
		self.defender = self.player

		self.hit_string = "hit"

		self.enemy_combat_string = "Combat has begun"
		self.player_combat_string = ""

		self.damage = 0


	def player_attack(self):
		"""
		Uses attack with the player as the attacker and sets the player_combat_string
		"""
		self.attack(self.player, self.enemy)
		self.player_combat_string = self.combat_description()

	def enemy_attack(self):
		"""
		Uses attack with the enemy as the attacker and sets the enemy_combat_string
		"""
		self.attack(self.enemy, self.player)
		self.enemy_combat_string = self.combat_description()


	def attack(self, attacker, defender):
		"""
		Updates attacker, changes hit_string, uses attack_damage to determine damage done 
		 and lowers defender hp appropriately

		Input:
			attacker <Player/Enemy>
			defender <Player/Enemy>

		Output:
			damage <int>
		# TBD allows a role to check if attacker hit
		"""
		hit = True
		self.attacker = attacker
		self.defender = defender
		self.hit_string = "missed"

		if hit:
			self.hit_string = "hit"
			self.damage = self.attack_damage(attacker)
			defender.hp -= self.damage
			return self.damage
			if self.attacker == self.enemy:
				self.enemy_combat_string = combat_description()

		return 0


	def attack_damage(self, attacker):
		"""
		Uses dice_roller common function to determine damage

		Input:
			attacker <Player/Enemy>

		Output:
			diceRoll <int>
		"""
		return dice_roller(attacker.weapon.quantity_of_die, attacker.weapon.damage_die_type, attacker.dmg_mod)

	def combat_description(self):
		"""
		Formats the information of the attacks in a string

		Output:
			combat_string <str>
		"""
		combat_string = "Most recently {} {} {} with {} and caused {} damage. {} now has {} HP remaining.\n".format(self.attacker.name,\
						self.hit_string, self.defender.name, self.attacker.weapon.name, self.damage, self.defender.name, self.defender.hp)

		return combat_string

