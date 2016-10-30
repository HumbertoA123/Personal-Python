#Tic-Tac-Toe Game

def place_x (x, possible):
	#Replace a number positiones on the board with X.
	board = """
		{}|{}|{}
		–––––
		{}|{}|{}
		–––––
		{}|{}|{}
		"""
	
	if x is 1:
		possible[1] = "X"
	if x is 2:
		possible[2] = "X"
	if x is 3:
		possible[3] = "X"
	if x is 4:
		possible[4] = "X"
	if x is 5:
		possible[5] = "X"
	if x is 6:
		possible[6] = "X"
	if x is 7:
		possible[7] = "X"
	if x is 8:
		possible[8] = "X"
	if x is 9:
		possible[9] = "X"

	print (board.format(possible[1], possible[2], possible[3], possible[4],
			possible[5], possible[6], possible[7], possible[8], possible[9]))


def place_o (x, possible):
	#Replace a number positioned on the board with O.
	board = """
		{}|{}|{}
		–––––
		{}|{}|{}
		–––––
		{}|{}|{}
		"""
	
	if x is 1:
		possible[1] = "O"
	if x is 2:
		possible[2] = "O"
	if x is 3:
		possible[3] = "O"
	if x is 4:
		possible[4] = "O"
	if x is 5:
		possible[5] = "O"
	if x is 6:
		possible[6] = "O"
	if x is 7:
		possible[7] = "O"
	if x is 8:
		possible[8] = "O"
	if x is 9:
		possible[9] = "O"

	print (board.format(possible[1], possible[2], possible[3], possible[4],
			possible[5], possible[6], possible[7], possible[8], possible[9]))


def position(possible, player):
	#Receives and input and check it to know if it is a valid input.
	position_value = False
	while position_value is False:
		try:
			x = int(input("Player {} turn: ".format(player)))
			if x >= 1 and x <= 9:
				if possible[x] != "X" and possible[x] != "O":
					position_value = True
				else:
					print ("That slot is already filled.")
			else:
				print ("Please type a valid input.")
		except ValueError:
			print ("Please type a valid input.")
	return x


def main ():
	#Main program.
	possible = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5,
				6 : 6, 7 : 7, 8 : 8, 9 : 9}
	print ("Tic-Tac-Toe")
	print ("Each player will type the number where they want to position their"
	 	+ " input.")
	print ("""
		1|2|3
		–––––
		4|5|6
		–––––
		7|8|9
		""")

	turn = 1
	for i in range(1, 10):
		#If i in the for loop gets to 9 then it is a tie.

		if (turn % 2 )!= 0:
			#If turn % 2 is different to 0 then it is X's turn.
			player = "X"
			pos = position(possible, player)
			place_x(pos, possible)
			#Possible win combinations.
			if possible[1] == player and possible[2] == player and possible[3] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[4] == player and possible[5] == player and possible[6] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[7] == player and possible[8] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[1] == player and possible[4] == player and possible[7] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[2] == player and possible[5] == player and possible[8] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[3] == player and possible[6] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[1] == player and possible[5] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[3] == player and possible[5] == player and possible[7] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			turn += 1

		elif (turn % 2) == 0:
			#If turn % 2 is equal to 0 then it is O's turn
			player = "O"
			pos = position(possible, player)
			place_o(pos, possible)
			#Possible win combinations.
			if possible[1] == player and possible[2] == player and possible[3] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[4] == player and possible[5] == player and possible[6] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[7] == player and possible[8] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[1] == player and possible[4] == player and possible[7] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[2] == player and possible[5] == player and possible[8] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[3] == player and possible[6] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[1] == player and possible[5] == player and possible[9] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			elif possible[3] == player and possible[5] == player and possible[7] == player:
				print ("Congratulations!")
				print ("Winner: Player {}".format(player))
				break
			turn += 1
		if i == 9:
			print ("Well it seem's that we have a tie.")

main()
