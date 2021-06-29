import numpy as np
import math

FILE_MOVE = "move.2.1000.txt"
FILE_PIECE = "piece.2.1000.txt"
FILE_BOARD = "board.2.1000.txt"



def save_board(checkers):
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

    file = open(FILE_BOARD, "a+")
    np.savetxt(file, num_list)
    file.close()

    return board_list


def load_board():
    input_data = np.loadtxt(FILE_BOARD).reshape(-1, 32)
    # print(input_data)

    return input_data


def save_piece(move):
    num = math.floor(move[0][0] * 4 + move[0][1] / 2)
    piece_list = [num]
    num_list = np.array(piece_list)

    file = open(FILE_PIECE, "a+")
    np.savetxt(file, num_list)
    file.close()

    return piece_list


def load_piece():
    input_data = np.loadtxt(FILE_PIECE)

    return input_data


def save_move(move):
    num = math.floor(move[1][0] * 4 + move[1][1] / 2)
    piece_list = [num]
    num_list = np.array(piece_list)

    file = open(FILE_MOVE, "a+")
    np.savetxt(file, num_list)
    file.close()

    return piece_list


def load_move():
    input_data = np.loadtxt(FILE_MOVE)

    return input_data
