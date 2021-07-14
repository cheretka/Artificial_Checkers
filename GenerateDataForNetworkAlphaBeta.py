from Checkers_state import *
from Algorithms.AlphaBeta import *
from MyNetwork import *
import math



if __name__ == "__main__":

    number_of_games = 1000
    red_experience = 7
    white_experience = 2
    sample = 15

    exp = 0
    for i in range(500):
        exp = 1
        print("\n\n------------------- ", (i + 1), " -----------------------\n\n")
        checkers = Checkers_state()

        while checkers.get_win() is None:

            selected_move = 0

            if checkers.get_current_player() == 'r':
                red_experience = math.ceil(exp/13) + 3
                if red_experience > 6:
                    red_experience = 6
                print("exp, ", exp, " - ", red_experience)
                selected_move = select_move(checkers, red_experience)
                print(save_board(checkers, sample, number_of_games), " ",
                      save_piece(selected_move, sample, number_of_games), " ",
                      save_move(selected_move, sample, number_of_games))
                exp += 1

            else:
                selected_move = select_move(checkers, white_experience)

            checkers = checkers.make_move(selected_move)




        print("win: " + checkers.get_win())
