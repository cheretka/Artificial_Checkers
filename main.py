from Board import *
import random
import time
from Minimax import *

# Function that takes a move from the user
def move_player(board):
    print('Turn  <' + board.current_player + '>  player')

    possible_moves, order = board.get_possible_moves()
    print("possible moves: ")
    print(possible_moves)

    good_move = False
    while not good_move:
        print("From which box to which [RowColumn RowColumn]? : ")
        start, end = map(int, sys.stdin.readline().split())
        move = [[start // 10, start % 10], [end // 10, end % 10]]
        # print(move)
        if move in possible_moves:
            board.make_move(move)
            good_move = True


# Function that selects and takes a step for the bot
def move_computer2(board):
    print('Turn  <' + board.current_player + '>  player')
    board.make_move(get_move(board))


def move_computer(board):
    print('Turn  <' + board.current_player + '>  player')
    print('AI turn')

    possible_moves, order = board.get_possible_moves()
    print("possible moves: ")
    print(possible_moves)

    board.make_move(random.choice(possible_moves))


if __name__ == "__main__":

    print('Welcome to English draughts (checkers)!')
    board = Board()
    board.print()

    # while board.get_win() is None:
    #     move_player(board)
    #     board.print()
    #
    # print("Win <" + board.get_win() + ">")

    # x=0
    while board.get_win() is None:
        if board.whose_turn() == 'r':
            move_computer2(board)
        else:
            move_computer2(board)
        board.print()
        time.sleep(0.2)

    print("Win <" + board.get_win() + ">")


    # print(board.get_win())
    # while board.get_win() is None:
    #     move_computer(board)
    #     board.print()
    #     time.sleep(0.2)
    #
    # print("Win <" + board.get_win() + ">")
