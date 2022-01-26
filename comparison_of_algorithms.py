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


def rand_first():
    print("---------------------------------  rand vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  rand vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  rand vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  rand vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  rand vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
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

    print("---------------------------------  rand vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = randomize(checkers)
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


def mm3_first():
    print("---------------------------------  mm3 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm3 vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm3 vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm3 vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm3 vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
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

    print("---------------------------------  mm3 vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 3)
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


def mm6_first():
    print("---------------------------------  mm6 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm6 vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm6 vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm6 vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mm6 vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
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

    print("---------------------------------  mm6 vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = minimax(checkers, 6)
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


def ab3_first():
    print("---------------------------------  ab3 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab3 vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab3 vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab3 vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab3 vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
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

    print("---------------------------------  ab3 vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 3)
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


def ab6_first():
    print("---------------------------------  ab6 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab6 vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab6 vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab6 vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  ab6 vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
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

    print("---------------------------------  ab6 vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = alphabeta(checkers, 6)
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


def mcts600_first():
    print("---------------------------------  mcts 600 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 600 vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 600 vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 600 vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 600 vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 600 vs mcts 1800  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 600)
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


def mcts1800_first():
    print("---------------------------------  mcts 1800 vs rand  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = randomize(checkers)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 1800 vs mm3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = minimax(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 1800 vs mm6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = minimax(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 1800 vs ab3  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = alphabeta(checkers, 3)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 1800 vs ab6  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
            else:
                selected_move = alphabeta(checkers, 6)
            checkers = checkers.make_move(selected_move)

        if checkers.get_win() == 'r':
            win += 1
        elif checkers.get_win() == 'remis':
            remis += 1
        else:
            lose += 1

        print("", win, ":", remis, ":", lose, "  =", i + 1)

    print("---------------------------------  mcts 1800 vs mcts 600  --------------------------------")

    win = 0
    remis = 0
    lose = 0
    for i in range(100):
        checkers = Checkers_state()

        while checkers.get_win() is None:
            if checkers.get_current_player() == 'r':
                selected_move = mcts(checkers, 1800)
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


if __name__ == "__main__":
    rand_first()

    mm3_first()
    mm6_first()

    ab3_first()
    ab6_first()

    mcts600_first()
    mcts1800_first()
