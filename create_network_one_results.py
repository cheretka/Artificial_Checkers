import numpy as np
import math
import time
import random
import Algorithms.Minimax
import Algorithms.AlphaBeta
import Algorithms.MCTS
from Checkers_state import *
from GetFromNetwork import *

def minimax(checkers, diff):
    return Algorithms.Minimax.select_move(checkers, diff)


def alphabeta(checkers, diff):
    return Algorithms.AlphaBeta.select_move(checkers, diff)


def mcts(checkers, diff):
    return Algorithms.MCTS.select_move(checkers, diff)


def randomize(checkers):
    possible_moves = checkers.get_possible_moves()
    return random.choice(possible_moves)



def check(network_move, all_moves):
    for move in all_moves:
        if move[0] == network_move[0] and move[1] == network_move[1]:
            return move

    return None



def net(checkers):
    selected_move = get_rezult_from_network_r(checkers)
    # print("selected_move ", selected_move)
    # print(checkers.get_possible_moves())
    # for move in checkers.get_possible_moves():
    #     print(move)

    selected_move = check(selected_move, checkers.get_possible_moves())
    if selected_move is None:
        # print("\n-------- the selected move is not possible -> MCTS  ")

        if len(checkers.get_possible_moves()) == 1:
            selected_move = checkers.get_possible_moves()[0]
        else:
            selected_move = Algorithms.MCTS.select_move(checkers, 1000)

    return selected_move







if __name__ == "__main__":

    # print("---------------------------------  net VS rand  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = net(checkers)
    #         else:
    #             selected_move = randomize(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    # print("---------------------------------  rand VS net  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = randomize(checkers)
    #         else:
    #             selected_move = net(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # print("---------------------------------  net VS mm3  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = net(checkers)
    #         else:
    #             selected_move = minimax(checkers, 3)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    # print("---------------------------------  mm3 VS net  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = minimax(checkers, 3)
    #         else:
    #             selected_move = net(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # print("---------------------------------  net VS mm6  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = net(checkers)
    #         else:
    #             selected_move = minimax(checkers, 6)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    # print("---------------------------------  mm6 VS net  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = minimax(checkers, 6)
    #         else:
    #             selected_move = net(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # print("---------------------------------  net VS ab3  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = net(checkers)
    #         else:
    #             selected_move = alphabeta(checkers, 3)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    # print("---------------------------------  ab3 VS net  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = alphabeta(checkers, 3)
    #         else:
    #             selected_move = net(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # print("---------------------------------  net VS ab6  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = net(checkers)
    #         else:
    #             selected_move = alphabeta(checkers, 6)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    # print("---------------------------------  ab6 VS net  --------------------------------")
    #
    # win = 0
    # remis = 0
    # lose = 0
    # for i in range(100):
    #     checkers = Checkers_state()
    #
    #     while checkers.get_win() is None:
    #         if checkers.get_current_player() == 'r':
    #             selected_move = alphabeta(checkers, 6)
    #         else:
    #             selected_move = net(checkers)
    #         checkers = checkers.make_move(selected_move)
    #
    #     if checkers.get_win() == 'r':
    #         win += 1
    #     elif checkers.get_win() == 'remis':
    #         remis += 1
    #     else:
    #         lose += 1
    #
    #     print("", win, ":", remis, ":", lose, "  =", i + 1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #






    print("---------------------------------  net VS mcts600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = net(checkers)
            else:
                selected_move = mcts(checkers, 600)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts600 VS net  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = net(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)











    print("---------------------------------  net VS mcts1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = net(checkers)
            else:
                selected_move = mcts(checkers, 1800)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts1800 VS net  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = net(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)