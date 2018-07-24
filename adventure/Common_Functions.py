import random

def dice_roller(quantity, die_sides, modifier):
	total_result = modifier
	for roll in range(0, quantity):
		die_roll = random.randint(0, die_sides)
		total_result += die_roll

	return (total_result)