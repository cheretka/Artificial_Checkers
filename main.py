from Checkers import *
import random
import time
from Minimax import *





def move_player(checkers):
    print('Turn  <' + checkers.current_player + '>  player')

    possible_moves = checkers.get_possible_moves()
    print("possible moves: ")
    print(possible_moves)

    good_move = False
    while not good_move:
        print("From which box to which [RowColumn RowColumn]? : ")
        start, end = map(int, sys.stdin.readline().split())
        move = [[start // 10, start % 10], [end // 10, end % 10]]
        if move in possible_moves:
            checkers.make_move(move)
            good_move = True




def move_computer2(checkers):
    print('Turn  <' + checkers.current_player + '>  player')
    checkers.make_move(get_move(checkers))




def move_computer(checkers):
    print('Turn  <' + checkers.current_player + '>  player')
    print('AI turn')

    possible_moves = checkers.get_possible_moves()
    print("possible moves: ")
    print(possible_moves)

    checkers.make_move(random.choice(possible_moves))



if __name__ == "__main__":
    print('Welcome to English draughts (checkers)!')
    checkers = Checkers()
    checkers.print()

    while checkers.get_win() is None:
        # if checkers.whose_turn() == 'r':
        #     move_computer2(checkers)
        # else:
        #     move_computer2(checkers)
        move_computer2(checkers)
        checkers.print()
        time.sleep(0.2)

    print("Win <" + checkers.get_win() + ">")


