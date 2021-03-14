from checkers.game import Game


#Create a new game:
game = Game()

#See whose turn it is:
game.whose_turn() #1 or 2

#Get the possible moves:
game.get_possible_moves() #[[9, 13], [9, 14], [10, 14], [10, 15], [11, 15], [11, 16], [12, 16]]

#Make a move:
game.move([9, 13])

#Check if the game is over:
game.is_over() #True or False

#Find out who won:
game.get_winner() #None or 1 or 2

#Review the move history:
game.moves #[[int, int], [int, int], ...]