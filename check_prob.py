import random
from deck import Deck

game_deck = Deck()
def run(fixed=False):
	counter = 1
	num_aces_pair = 0
	stop_limit = 1000
	while True:
		# Shuffle deck
		random.shuffle(game_deck.deck)
		# Take 2 cards from the top
		hand = game_deck.deck[0:2]
		# Check if both cards are Aces, 
		if hand[0][0] == 'A' and hand[1][0] == 'A':
			if fixed == False:
				return 1/counter
			else:
				num_aces_pair += 1
		counter += 1
		if counter > stop_limit:
			return num_aces_pair/counter