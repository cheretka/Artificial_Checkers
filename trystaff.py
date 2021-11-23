import numpy as np
import math
import time
from Algorithms.Minimax import *
from Checkers_state import *





if __name__ == "__main__":
    start = time.time()

    checkers = Checkers_state()
    checkers.print()

    # print("start")
    #
    #
    # for i in range(9, 15):
    #     print("i=", i)
    #     checkers = Checkers_state()
    #     # checkers.print()
    #     start = time.time()
    #
    #     selected_move = select_move(checkers, i)
    #
    #     end = time.time()
    #     print(i, " ", end - start, "\n")
    #
    #
    #
    # end = time.time()
    # print("the end time: ")
    # print(end - start)

