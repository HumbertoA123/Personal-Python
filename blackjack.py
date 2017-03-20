import random
import os

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,]


class Dealer (object):


	def __init__ (self, cards = []):
		self.cards = cards

	def add_card (self):
		self.cards.append(deck.pop(random.randrange(0, len(deck))))
		#Removes a card from the deck and place it in the player's cards.
		return self.cards

	def sum_cards (self):
		#Sum the values of the cards in the dealer's hand.
		return sum(self.cards)

	def another_card (self, dealer):
			while True:
				dealer.add_card()
				if dealer.sum_cards() >= 17:
					break
			print ('Dealer Cards: {}	Total sum: {}'.format(dealer.cards, dealer.sum_cards()))
		


class Player (object):


	def __init__ (self, chips = 100, bet = 5, cards = []):
		self.chips = chips
		self.cards = cards

	def bet (self, bet):
		self.bet = bet

	def add_card (self):
		self.cards.append(deck.pop(random.randrange(0, len(deck))))
		#Removes a card from the deck and place it in the player's cards.
		return self.cards

	def sum_cards (self):
		#Sum the values of the cards in your hand.
		return sum(self.cards)

	def another_card (self, player):
		while player.sum_cards() < 21:
			s = input('Do you want another card? (yes or no): ')
			try:
				if s[0].lower() == 'y':
					#Checks if the first letter of your answer is 'y'.
					player.add_card()
					print ('Player Cards: {}	Total sum: {}'.format(player.cards, player.sum_cards()))
					if player.sum_cards() >= 21:
						#Checks if the sum of your cards is 21 or more.
						break
				elif s[0] == 'n':
				#Checks if the first letter of your answer is 'n'.
					break
			except:
				print ('That is not a valid input.')


def to_win (player, dealer):
	if dealer.sum_cards() <= 21 and player.sum_cards() <= 21:
		dealer.another_card(dealer)

	if player.sum_cards() > 21:
		print ('The house won.')

	elif dealer.sum_cards() > 21:
		print ('Congratulation! You won.')
		player.chips += (player.bet * 2)

	elif player.sum_cards() > dealer.sum_cards():
		print ('Congratulations! You won.')
		player.chips += (player.bet * 2)

	elif player.sum_cards() < dealer.sum_cards():
		print ('The house won.')

	elif player.sum_cards() == dealer.sum_cards():
		print ('We have a tie.')
		player.chips += player.bet


def cash_input ():
	while True:
		try:
			cash = int(input('How many chips do you want to buy: '))
			break
		except ValueError:
			print ('Invalid input.')
	return cash




def main ():
	#Main Program.
	print('{:^100}'.format('Blackjack\n'))

	cash = cash_input()
	player = Player(chips = cash)
	dealer = Dealer()

	while True:
		print ('Total Chips: {}'.format(player.chips))

		while True:
			try:
				initial_bet = int(input('Place your initial bet: '))
				player.bet = initial_bet
				if player.bet > player.chips:
					print ("Not enough chips")
				else:
					player.bet = initial_bet
					break

			except ValueError:
				print ('Invalid input')


		player.chips -= player.bet
		print ('Chips: {}'.format(player.chips))
		print ('Total bet: {}'.format(player.bet))


		player.cards = []
		dealer.cards = []


		dealer.add_card()
		player.add_card()
		player.add_card()

		print ('Player Cards: {}	Total sum: {}'.format(player.cards, player.sum_cards()))
		print ('Dealer Cards: {}	Total sum: {}'.format(dealer.cards, dealer.sum_cards()))

		player.another_card(player)
		to_win(player, dealer)

		play_again = input('Do you want to play another match? (yes or no): ')
		if play_again[0].lower() == 's':
			#Checks if the player wants to keep playing.
			#If player wants to keep playing, it resets the cards.
			dealer = Dealer(cards = [])
			player = Player(cards = [])
		elif play_again[0].lower() == 'n':
			#If player doesn't want to keep playing then the game is over.
			break

		if player.chips == 0:
			print ('You ran out of chips.')
			keep_playing = input('Do you want to buy more chips? (yes or no): ')
			if keep_playing[0].lower() == 'y':
				cash = int(input('How many chips do you want to buy: '))
				player.chips += cash
			else:
				break
			
		os.system('cls' if os.name == 'nt' else 'clear')

		print('{:^100}'.format('Blackjack\n'))

main()