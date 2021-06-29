from Checkers_state import *
import random
import time
# from Minimax import *
# from AlphaBeta import *
# from MCTS import *
from MCTS import *
from Savery import *


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


def move_computer(checkers, diff):
    # print('Turn  <' + checkers.current_player + '>  player')
    move = get_move(checkers, diff)
    checkers.make_move(move)


def move_computer_random(checkers):
    print('Turn  <' + checkers.current_player + '>  player')
    print('AI turn')

    possible_moves = checkers.get_possible_moves()
    print("possible moves: ")
    print(possible_moves)

    checkers.make_move(random.choice(possible_moves))


def fun1(board):
    # determination for which mark the person and AI will play
    # human_letter = ''
    # while not (human_letter == 'A' or human_letter == 'R'):
    #     print('Do you want to be \'A\' (moves first) or \'R\' ?')
    #     human_letter = input().upper()

    while checkers.get_win() is None:
        move_player(checkers)

    print("Win <" + checkers.get_win() + ">")


def fun2(board):
    # determination for which mark the person and AI will play
    human_letter = ''
    while not (human_letter == 'A' or human_letter == 'R'):
        print('Do you want to be \'A\' (moves first) or \'R\' ?')
        human_letter = input().upper()

    while checkers.get_win() is None:
        if checkers.whose_turn() == human_letter.lower():
            move_player(checkers)
        else:
            move_computer(checkers, 4)
        checkers.print()

    print("Win <" + checkers.get_win() + ">")


def fun3(board):
    # determination for which mark the person and AI will play
    human_letter = ''
    while not (human_letter == 'A' or human_letter == 'R'):
        print('Do you want to be \'A\' (moves first) or \'R\' ?')
        human_letter = input().upper()

    while checkers.get_win() is None:
        if checkers.whose_turn() == human_letter.lower():
            move_player(checkers)
        else:
            move_computer(checkers, 9)
        checkers.print()

    print("Win <" + checkers.get_win() + ">")


def fun4(board):
    while checkers.get_win() is None:
        move = get_move(checkers, 14)
        checkers.make_move(move)

        checkers.print()
        time.sleep(0.1)

    print(checkers.get_win())


# def fun4(board):
#
#     while checkers.get_win() is None:
#         move = select_move(checkers, 10)
#         checkers.make_move(move)
#
#         checkers.print()
#         time.sleep(0.1)
#
#     print(checkers.get_win())


if __name__ == "__main__":

    for i in range(1000):
        print("\n\n------------------- ", i, " -----------------------\n\n")

        print('Welcome to English draughts (checkers)!')
        checkers = Checkers_state()
        checkers.print()

        while checkers.get_win() is None:

            if checkers.get_current_player() == 'r':

                print(save_board(checkers))

                movesss = select_move(checkers, 1500)

                print(save_piece(movesss))
                print(save_move(movesss))

                checkers = checkers.make_move(movesss)
                # checkers.print(movesss[0])
            else:
                movesss = select_move(checkers, 100)
                checkers = checkers.make_move(movesss)
                # checkers.print(movesss[0])

        print("win: " + checkers.get_win())
