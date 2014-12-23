import random

def weighted_random():

	letters = [

	(0.079971, 'A'), (0.020199, 'B'), (0.043593, 'C'),
	(0.032184, 'D'), (0.112513, 'E'), (0.014622, 'F'),
	(0.022845, 'G'), (0.023497, 'H'), (0.08563,  'I'),
	(0.001693, 'J'), (0.008535, 'K'), (0.060585, 'L'),
	(0.028389, 'M'), (0.071596, 'N'), (0.065476, 'O'),
	(0.029165, 'P'), (0.00183,  'Q'), (0.07264,  'R'),
	(0.066044, 'S'), (0.070926, 'T'), (0.037091, 'U'),
	(0.011369, 'V'), (0.008899, 'W'), (0.002925, 'X'),
	(0.024432, 'Y'), (0.00335,  'Z'),

	]

	total = sum(w for w, c in letters)
	print total
	r = random.uniform(0, 1)
	print r
	upto = 0
	for w, c in letters:
		print "UPTO = " + str(upto)
		if upto + w > r:
			return c

		upto += w
	assert False, "Shouldn't get here"

def get_letter_set():
	letters = []
	for x in range(8):
		letters.append(weighted_random())
	print letters

get_letter_set()