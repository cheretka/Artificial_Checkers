import numpy as np
import math


def save_board(checkers, sample, number_of_games):
    board_list = []

    for i in range(len(checkers.board)):
        for j in range(len(checkers.board[i])):

            if (i + j) % 2 == 0:
                continue

            element = checkers.board[i][j]
            if element == 'A':
                board_list.append(0)
            elif element == 'a':
                board_list.append(1)
            elif element == ' ':
                board_list.append(2)
            elif element == 'r':
                board_list.append(3)
            elif element == 'R':
                board_list.append(4)

    num_list = np.array(board_list)

    file = open("board." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
    np.savetxt(file, num_list)
    file.close()

    return board_list


def load_board(sample, number_of_games):
    input_data = np.loadtxt("board." + str(sample) + "." + str(number_of_games) + ".txt").reshape(-1, 32)
    # print(input_data)

    return input_data


def save_piece(move, sample, number_of_games):
    num = math.floor(move[0][0] * 4 + move[0][1] / 2)
    piece_list = [num]
    num_list = np.array(piece_list)

    file = open("piece." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
    np.savetxt(file, num_list)
    file.close()

    return piece_list


def load_piece(sample, number_of_games):
    input_data = np.loadtxt("piece." + str(sample) + "." + str(number_of_games) + ".txt")

    return input_data


def save_move(move, sample, number_of_games):
    num = math.floor(move[1][0] * 4 + move[1][1] / 2)
    piece_list = [num]
    num_list = np.array(piece_list)

    file = open("move." + str(sample) + "." + str(number_of_games) + ".txt", "a+")
    np.savetxt(file, num_list)
    file.close()

    return piece_list


def load_move(sample, number_of_games):
    input_data = np.loadtxt("move." + str(sample) + "." + str(number_of_games) + ".txt")

    return input_data
