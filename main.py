from Checkers_state import *
import random
import time
# from Minimax import *
# from AlphaBeta import *
# from MCTS import *
from MCTS import *




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
    print('Welcome to English draughts (checkers)!')
    checkers = Checkers_state()
    checkers.print()

    # while checkers.get_win() is None:
    #
    #     possible_moves = checkers.get_possible_moves()
    #     print()
    #     print("possible moves: ")
    #     print(possible_moves)
    #     movesss = get_move(checkers, 5)
    #
    #     print("turn: " + checkers.get_current_player())
    #     checkers = checkers.make_move(movesss)
    #     checkers.print(movesss[0])
    #
    # print("win: " + checkers.get_win())


    while checkers.get_win() is None:
    # for i in range(5):
        movesss = select_move(checkers, 1000)
        print(movesss)

        print("turn: " + checkers.get_current_player())
        checkers = checkers.make_move(movesss)
        checkers.print(movesss[0])

    print("win: " + checkers.get_win())