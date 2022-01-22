import numpy as np
import math


def save_board_to_file(board, file_name):
    file = open(file_name, "a+")
    np.savetxt(file, board)
    file.close()

    return board


def save_smth_to_file(smth, file_name):
    num_list = np.array([smth])
    file = open(file_name, "a+")
    np.savetxt(file, num_list)
    # file.write(str(smth))
    file.close()

    return num_list


def load_board_from_file(file_name):
    input_data = np.loadtxt(file_name).reshape(-1, 32)

    return input_data


def load_smth_from_file(file_name):
    input_data = np.loadtxt(file_name)

    return input_data

# def save_board(board, file_name):
#
#     file = open(file_name, "a+")
#     np.savetxt(file, board)
#     file.close()
#
#     return board_list
#
# def save_piece(piece, file_name):
#
#     file = open(file_name, "a+")
#     np.savetxt(file, piece)
#     file.close()
#
#     return piece_list
#
# def save_move(move, file_name):
#
#     file = open(file_name, "a+")
#     np.savetxt(file, move)
#     file.close()
#
#     return piece_list


# def save_board(checkers, sample, number_of_games):
#     board_list = []
#
#     for i in range(len(checkers.board)):
#         for j in range(len(checkers.board[i])):
#
#             if (i + j) % 2 == 0:
#                 continue
#
#             element = checkers.board[i][j]
#             if element == 'A':
#                 board_list.append(0)
#             elif element == 'a':
#                 board_list.append(1)
#             elif element == ' ':
#                 board_list.append(2)
#             elif element == 'r':
#                 board_list.append(3)
#             elif element == 'R':
#                 board_list.append(4)
#
#     num_list = np.array(board_list)
#
#     file = open("board." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
#     np.savetxt(file, num_list)
#     file.close()
#
#     return board_list
#
#
# def load_board(sample, number_of_games):
#     input_data = np.loadtxt("board." + str(sample) + "." + str(number_of_games) + ".txt").reshape(-1, 32)
#     # print(input_data)
#
#     return input_data
#
#
# def save_piece(move, sample, number_of_games):
#     num = math.floor(move[0][0] * 4 + move[0][1] / 2)
#     piece_list = [num]
#     num_list = np.array(piece_list)
#
#     file = open("piece." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
#     np.savetxt(file, num_list)
#     file.close()
#
#     return piece_list
#
#
# def load_piece(sample, number_of_games):
#     input_data = np.loadtxt("piece." + str(sample) + "." + str(number_of_games) + ".txt")
#
#     return input_data
#
#
# def save_move(move, sample, number_of_games):
#     num = math.floor(move[1][0] * 4 + move[1][1] / 2)
#     piece_list = [num]
#     num_list = np.array(piece_list)
#
#     file = open("move." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
#     np.savetxt(file, num_list)
#     file.close()
#
#     return piece_list
#
#
# def load_move(sample, number_of_games):
#     input_data = np.loadtxt("move." + str(sample) + "." + str(number_of_games) + ".txt")
#
#     return input_data
