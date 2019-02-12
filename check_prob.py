import random
from deck import Deck

game_deck = Deck()
def run():
	counter = 1
	while True:
		# Shuffle deck
		random.shuffle(game_deck.deck)
		# Take 2 cards from the top
		hand = game_deck.deck[0:2]
		# print(f"{counter}: {hand}")
		# Check if both cards are Aces, 
		if hand[0][0] == 'A' and hand[1][0] == 'A':
			#print("BAN BAN!")
			#print(1/counter)
			return 1/counter	
		counter += 1