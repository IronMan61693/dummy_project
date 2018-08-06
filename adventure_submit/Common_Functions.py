import random

def dice_roller(quantity, die_sides, modifier):
	"""
	Uses random to provide a number of a quantity die rolled with die_sides number of sides
	 Adds the modifier to the result

	Input:
		quantity <int>
		die_sides <int>
		modifier <int>

	Output:
		total_result <int>
	"""
	total_result = modifier
	for roll in range(0, quantity):
		die_roll = random.randint(1, die_sides)
		total_result += die_roll

	return total_result