import random
import sqlite3
import sys
import time
from time import strftime

DB_FILE1 = 'scores.db'
DB_FILE2 = 'dictionary.db'

values =  {
				'a': 3, 'b': 10, 'c': 7, 'd': 9, 'e': 1,
			   'f': 10, 'g': 9, 'h': 9, 'i': 4, 'j': 12,
			   'k': 6, 'l': 2, 'm': 9, 'n': 5, 'o': 5, 'p': 9, 
			   'q': 12, 'r': 4, 's': 6, 't': 5, 'u': 8, 
			   'v': 11, 'w': 11, 'x': 12, 'y': 10, 'z': 12 
		}

word = 'alamo'

def get_points_sum(word):
	s = 0

	for x in word:
		s += values.get(x)
	return s

def scoring_algs(word):
	s = get_points_sum(word)
	n = len(word)


	formulas = {
    	1: (1, 0),
    	2: (20, 2000),
    	3: (70, 7000),
    	4: (80, 8000),
    	5: (100, 10000),
    	6: (120, 12000),
    	7: (140, 15000),
    	8: (180, 20000),
    	9: (220, 25000),
    	10: (260, 30000),
    	11: (350, 40000),
    	12: (440, 50000)
	}

	factor, offset = formulas[n]
	return factor * s + offset


def top_scores():
	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS Scores
					(id INTEGER PRIMARY KEY AUTOINCREMENT,
					 player_name text,
					 score_date timestamp,
					 score integer)''')

def add_score(score, name):
	now = strftime("%Y-%m-%d %H:%M:%S")
	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()

	c.execute('''INSERT INTO Scores (score_date, score, player_name)
	 						VALUES (?, ?, ?)''', (now, score, name))
	conn.commit()
	conn.close()

def timer():
	for t in range(120, -1, -1):
		m = t / 60
		s = t % 60
		end = sys.stdout.write("%d:%d \r" % (m,s))
		time.sleep(1.0)
		sys.stdout.flush()
		if end == 0:
			break



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

	total = sum(x for x, y in letters)
	r = random.uniform(0, total)
	upto = 0
	for x, y in letters:
		if upto + x > r:
			return y
		upto += x
	assert False, "NO"

def get_letter_set():
	letters = []
	for x in range(8):
		letters.append(weighted_random())
	return letters

def test_player_word(word):
	conn = sqlite3.connect(DB_FILE2)
	c = conn.cursor()

	valid_word = c.execute('''SELECT * FROM Dictionary 
							  WHERE word=?''', (word))

	return valid_word

def test_letter_set(word, letter_set):
	for x in word:
		if x in letter_set:
			letter_set.remove(x)
		else:
			return False


def play():
	total_score = 0
	top_scores()
	name = raw_input('name: ')
	letters = get_letter_set()
	print letters

	while True:
		word = raw_input('enter word: ')
		if test_player_word(word) and test_letter_set(word, letters):
			score = scoring_algs(word)
			print word + " equals " + str(score) + "points"
			total_score += score
			print "Total score: " + str(total_score) + "points"












