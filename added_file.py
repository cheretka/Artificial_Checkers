from tensorflow import keras
from tensorflow.keras import layers
from Savery import *
import random
from a_play_games import *
from ab_fit_all_models import *
import GetFromNetwork
import numpy as np
import math
import a_play_games


if __name__ == "__main__":

    fit_piece_network_bad_choice()
    fit_move_network_bad_choice()
    fit_piece_network_good_choice()
    fit_move_network_good_choice()

    print("end")



    # checkers = Checkers_state()
    # model_piece = keras.models.load_model("model_piece_3")
    # model_move = keras.models.load_model("model_move_3")
    #
    # checkers.board = [[' ', 'r', ' ', ' ', ' ', 'r', ' ', 'r'],
    #               [' ', ' ', 'r', ' ', ' ', ' ', ' ', ' '],
    #               [' ', 'a', ' ', ' ', ' ', 'r', ' ', 'r'],
    #               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #               [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a'],
    #               [' ', ' ', ' ', ' ', 'r', ' ', ' ', ' '],
    #               [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a'],
    #               ['a', ' ', 'R', ' ', 'a', ' ', 'a', ' ']]
    #
    # checkers.print()
    # checkers.current_player = "a"
    #
    # a_board_2, a_piece_2, a_move_2 = get_rezult_from_network(checkers, model_piece, model_move, 0)
    # print(a_board_2)
    # print(a_piece_2)
    # print(a_move_2)
    #
    # x1 = math.floor(a_piece_2 / 4)
    # x2 = ((a_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((a_piece_2 % 4) * 2)
    # y1 = math.floor(a_move_2 / 4)
    # y2 = ((a_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((a_move_2 % 4) * 2)
    # # selected_move1 = [[x1, x2], [y1, y2]]
    # selected_move = [[7 - x1, 7 - x2], [7 - y1, 7 - y2]]
    # print(selected_move)

    # possible_moves = checkers.get_possible_moves()
    # selected_move = random.choice(possible_moves)
    #
    # checkers = checkers.make_move(selected_move)
    # checkers.print(selected_move[0])


#
#
# def fit_move_network_bad_choice():
#     print("\nstart - fit_move_network_bad_choice")
#
#
#
#     print("Load board")
#
#     boards = load_board_from_file("m_faulty_board.txt")
#     # print("shape ", boards.shape)
#
#     rand_indexes = random.sample(range(len(boards)), 1024)
#     train_input = []
#     for index in rand_indexes:
#         train_input.append(boards[index])
#     train_input = np.array(train_input)
#     train_input = train_input.astype('float32') / 5
#     # print("train_input ", train_input)
#     # print("shape ", train_input.shape)
#
#
#
#     print("Load pieces")
#     piece_tables = np.zeros((1024, 32))
#     pieces = load_smth_from_file("m_faulty_piece.txt")
#     pieces = pieces.astype('int')
#     # print("pieces ", pieces)
#     # print("shape ", pieces.shape)
#
#     train_pieces = []
#     for index in rand_indexes:
#         train_pieces.append(pieces[index])
#     # print("pieces ", train_pieces)
#     # print("shape ", len(train_pieces))
#
#     for i in range(len(piece_tables)):
#         piece_tables[i][train_pieces[i]] = 1
#
#     # print("piece_tables ", piece_tables)
#     # print("shape ", piece_tables.shape)
#
#
#     model = keras.models.load_model("model_move_3")
#     train_output_move = model.predict([train_input, piece_tables])
#
#     print("Load moves")
#     moves = load_smth_from_file("m_faulty_move.txt")
#     moves = moves.astype('int')
#     # print("moves ", moves)
#     # print("shape ", moves.shape)
#
#     train_moves = []
#     for index in rand_indexes:
#         train_moves.append(moves[index])
#     # print("train_moves ", train_moves)
#     # print("shape ", len(train_moves))
#
#
#     for i in range(len(train_output_move)):
#         train_output_move[i][train_moves[i]] = -1
#
#     # print("train_output_move ", train_output_move)
#     # print("shape ", train_output_move.shape)
#
#     print('train model')
#     history = model.fit([train_input, piece_tables],
#                         y=train_output_move,
#                         batch_size=32,
#                         epochs=1)
#
#     print('history dict:', history.history)
#
#     model.save("model_move_3")
#
#     print("end - fit_move_network_bad_choice\n")
#
