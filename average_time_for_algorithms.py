import numpy as np
import math
import time
import random
import Algorithms.Minimax
import Algorithms.AlphaBeta
import Algorithms.MCTS
from Checkers_state import *


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

    # print("\n---------------------------------  rand  --------------------------------")
    #
    # suma = 0.0
    # n = 0
    # for i in range(30):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         n = n+1
    #         start = time.time()
    #
    #         selected_move = randomize(checkers)
    #
    #         end = time.time()
    #         suma = suma + (end - start)
    #
    #         checkers = checkers.make_move(selected_move)
    #     print(n)
    #
    # average = suma / n
    # print("---------  rand  ----------  ", suma, "(s) / ", n, " = ", average, "(s)")
    #
    #



    for iter in range(5, 9):
        print("\n\n---------------------------------  mm", iter, "  --------------------------------")

        suma = 0.0
        n = 0
        for i in range(3):
            checkers = Checkers_state()

            while checkers.get_win() is None:
                n = n + 1
                start = time.time()

                selected_move = minimax(checkers, iter)

                end = time.time()
                suma = suma + (end - start)

                checkers = checkers.make_move(selected_move)
            print(n)

        average = suma / n
        print("---------  mm", iter, "  ----------  ", suma, "(s) / ", n, " = ", average, "(s)")




    for iter in range(5, 9):
        print("\n\n---------------------------------  ab", iter, "  --------------------------------")

        suma = 0.0
        n = 0
        for i in range(3):
            checkers = Checkers_state()

            while checkers.get_win() is None:
                n = n + 1
                start = time.time()

                selected_move = alphabeta(checkers, iter)

                end = time.time()
                suma = suma + (end - start)

                checkers = checkers.make_move(selected_move)
            print(n)

        average = suma / n
        print("---------  ab", iter, "  ----------  ", suma, "(s) / ", n, " = ", average, "(s)")



    #
    # for iter in range(100, 2500, 100):
    #     print("\n\n---------------------------------  mcts", iter, "  --------------------------------")
    #
    #     suma = 0.0
    #     n = 0
    #     for i in range(30):
    #         checkers = Checkers_state()
    #
    #         while checkers.get_win() is None:
    #             n = n + 1
    #             start = time.time()
    #
    #             selected_move = mcts(checkers, iter)
    #
    #             end = time.time()
    #             suma = suma + (end - start)
    #
    #             checkers = checkers.make_move(selected_move)
    #         print(n)
    #
    #     average = suma / n
    #     print("---------  mcts", iter, "  ----------  ", suma, "(s) / ", n, " = ", average, "(s)")