from Checkers import *
import random
import time
# from Minimax import *
from AlphaBeta import *




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
    # print(move)
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
    human_letter = ''
    while not (human_letter == 'A' or human_letter == 'R'):
        print('Do you want to be \'A\' (moves first) or \'R\' ?')
        human_letter = input().upper()

    while checkers.get_win() is None:
        if checkers.whose_turn() == human_letter.lower():
            move_player(checkers)
        else:
            move_computer_random(checkers)
        checkers.print()

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
            move_computer(checkers, 8)
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
            move_computer(checkers, 15)
        checkers.print()

    print("Win <" + checkers.get_win() + ">")



def fun4(board):
    while checkers.get_win() is None:
        move_computer(checkers, 10)
        # checkers.print()
        # time.sleep(0.1)

    print( checkers.get_win())



if __name__ == "__main__":
    # print('Welcome to English draughts (checkers)!')
    # checkers = Checkers()
    # checkers.print()
    #
    # print('choose one option:')
    # print('1 - play with bot (easy level)')
    # print('2 - play with bot (medium level)')
    # print('3 - play with bot (hard level)')
    # print('4 - game between two bots (hard level)')
    # choose = int(input())
    #
    # if choose == 1:
    #     fun1(checkers)
    # if choose == 2:
    #     fun2(checkers)
    # if choose == 3:
    #     fun3(checkers)
    # if choose == 4:
    #     fun4(checkers)


    for i in range(1000):
        checkers = Checkers()
        # checkers.print()
        fun4(checkers)


