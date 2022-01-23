from a_play_games import *
from ab_fit_all_models import *
from GetFromNetwork import *




if __name__ == "__main__":


    for i in range(1):

        printf("\n", i, "  iteracja")

        # play
        play_game_and_write_moves()
        play_rand_game_and_write_moves()

        # fit
        # fit_piece_network_bad_choice()
        # fit_move_network_bad_choice()

        # fit_piece_network_good_choice()
