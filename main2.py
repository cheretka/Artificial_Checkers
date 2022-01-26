from a_play_games import *
from ab_fit_all_models import *
import GetFromNetwork
import numpy as np
import math
import a_play_games


if __name__ == "__main__":

    # set values for count lines in files

    data_from_file = np.loadtxt("p_faulty_piece.txt")
    n1 = len(data_from_file)
    GetFromNetwork.ile_p_bad = n1
    data_from_file = np.loadtxt("m_faulty_piece.txt")
    n2 = len(data_from_file)
    GetFromNetwork.ile_m_bad = n2
    data_from_file = np.loadtxt("correct_piece_1.txt")
    n3 = len(data_from_file)
    a_play_games.ile_good = n3



    for i in range(1):

        # play
        # play_rand_game_and_write_moves()

        # fit
        fit_piece_network_bad_choice()
        fit_move_network_bad_choice()
        fit_piece_network_good_choice()
        fit_move_network_good_choice()

        # check
        # play_game_and_write_moves()
