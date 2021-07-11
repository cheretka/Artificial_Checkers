from Checkers_state import *
import time
# from Minimax import *
# from AlphaBeta import *
# from MCTS import *
from Algorithms.MCTS import *
from MyNetwork import *


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


def check(network_move, all_moves):
    for move in all_moves:
        if move[0] == network_move[0] and move[1] == network_move[1]:
            return move

    return None



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


    while checkers.get_win() is None:

        selected_move = 0

        if checkers.get_current_player() == 'r':

            selected_move = get_move_from_network(checkers)
            print("selected_move ", selected_move)
            for move in checkers.get_possible_moves():
                print(move)

            selected_move = check_move(selected_move, checkers.get_possible_moves())
            if selected_move == None:
                print("\n!! the selected move is not possible !!\n")
                break
        else:
            # selecte move by MCTS
            selected_move = select_move(checkers, white_experience)


        checkers = checkers.make_move(selected_move)
        checkers.print(selected_move[0])


        print()

    if checkers.get_win() is not None:
        print("win: " + checkers.get_win())
