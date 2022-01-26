import numpy as np
import math
import time
import Algorithms.Minimax
import Algorithms.AlphaBeta
import Algorithms.MCTS
from Checkers_state import *
import random



def minimax(checkers, diff):
    return Algorithms.Minimax.select_move(checkers, diff)

def alphabeta(checkers, diff):
    return Algorithms.AlphaBeta.select_move(checkers, diff)

def mcts(checkers, diff):
    return Algorithms.MCTS.select_move(checkers, diff)

def randomize(checkers):
    possible_moves = checkers.get_possible_moves()
    return random.choice(possible_moves)


if __name__ == "__main__":


    # print("---------------------------------  mcts1800 VS rand  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    #
    # # play 100 games
    # for i in range(100):
    #
    #     # create new board
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #
    #         # if current player is BOT
    #         if checkers.get_current_player() == 'r':
    #             selected_move = mcts(checkers, 1800)
    #
    #         else:
    #             selected_move = randomize(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     #count results
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     # print statistics
    #     print("", win, ":", remis, ":", lose, "  =", i+1)


    print("---------------------------------  mcts1800 VS mcts600  --------------------------------")

    win = 0
    remis = 0
    lose = 0

    # play 100 games
    for i in range(100):

        # create new board
        checkers = Checkers_state()

        while checkers.get_win() is None:

            # if current player is BOT
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)

            else:
                selected_move = mcts(checkers, 600)
            checkers = checkers.make_move(selected_move)

        #count results
        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        # print statistics
        print("", win, ":", remis, ":", lose, "  =", i+1)



