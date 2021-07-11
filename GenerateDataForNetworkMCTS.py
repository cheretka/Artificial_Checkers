from Checkers_state import *
from Algorithms.MCTS import *
from MyNetwork import *

if __name__ == "__main__":

    number_of_games = 1000
    red_experience = 1000
    white_experience = 100
    sample = 0

    for i in range(number_of_games):
        print("\n\n------------------- ", (i + 1), " -----------------------\n\n")
        checkers = Checkers_state()

        while checkers.get_win() is None:

            selected_move = 0

            if checkers.get_current_player() == 'r':
                selected_move = select_move(checkers, red_experience)
                print(save_board(checkers, sample, number_of_games), " ",
                      save_piece(selected_move, sample, number_of_games), " ",
                      save_move(selected_move, sample, number_of_games))

            else:
                selected_move = select_move(checkers, white_experience)

            checkers = checkers.make_move(selected_move)

            # print()

        print("win: " + checkers.get_win())
