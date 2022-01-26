import NetworkMove
import NetworkPiece
import copy
import main2
import numpy as np
import math
from Savery import *
import random

count_of_bad_moves = 0


def get_count_of_bad_moves():
    global count_of_bad_moves
    return count_of_bad_moves


def zero_count_of_bad_moves():
    global count_of_bad_moves
    count_of_bad_moves = 0
    return count_of_bad_moves


ile_p_bad = 0
ile_m_bad = 0


def write_to_file_bad_piece(board, piece):
    global ile_p_bad

    if ile_p_bad >= 100000:
        data_from_file = np.loadtxt("p_faulty_piece.txt")
        file = open("p_faulty_piece.txt", "w")
        np.savetxt(file, data_from_file[30000:])
        file.close()

        data_from_file = np.loadtxt("p_faulty_board.txt")
        file = open("p_faulty_board.txt", "w")
        np.savetxt(file, data_from_file[(32 * 30000):])
        file.close()

        ile_p_bad -= 30000

    save_board_to_file(board, "p_faulty_board.txt")
    save_smth_to_file(piece, "p_faulty_piece.txt")
    ile_p_bad += 1


def write_to_file_bad_move(board, piece, move):
    global ile_m_bad

    if ile_m_bad >= 100000:

        data_from_file = np.loadtxt("m_faulty_piece.txt")
        file = open("m_faulty_piece.txt", "w")
        np.savetxt(file, data_from_file[30000:])
        file.close()

        data_from_file = np.loadtxt("m_faulty_move.txt")
        file = open("m_faulty_move.txt", "w")
        np.savetxt(file, data_from_file[30000:])
        file.close()

        data_from_file = np.loadtxt("m_faulty_board.txt")
        file = open("m_faulty_board.txt", "w")
        np.savetxt(file, data_from_file[(32 * 30000):])
        file.close()

        ile_m_bad -= 30000

    save_board_to_file(board, "m_faulty_board.txt")
    save_smth_to_file(piece, "m_faulty_piece.txt")
    save_smth_to_file(move, "m_faulty_move.txt")
    ile_m_bad += 1


def get_rezult_from_network(checkers, model_piece, model_move, is_net_and_net):
    global count_of_bad_moves

    board_2 = copy.deepcopy(checkers.board)
    board_list = []

    if checkers.get_current_player() == "a":

        board_2.reverse()
        for i in range(len(board_2)):
            board_2[i].reverse()

        for i in range(len(board_2)):
            for j in range(len(board_2[i])):
                if board_2[i][j] == 'A':
                    board_2[i][j] = 'R'
                elif board_2[i][j] == 'a':
                    board_2[i][j] = 'r'
                elif board_2[i][j] == 'R':
                    board_2[i][j] = 'A'
                elif board_2[i][j] == 'r':
                    board_2[i][j] = 'a'

    for i in range(len(board_2)):
        for j in range(len(board_2[i])):

            if (i + j) % 2 == 0:
                continue

            element = board_2[i][j]
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
    train_input = num_list.astype('float32') / 5
    train_input = np.reshape(train_input, (1, 32))

    predictions_piece = model_piece.predict(train_input)
    predictions_piece = predictions_piece[0]

    possible_moves = checkers.get_possible_moves()

    if checkers.get_current_player() == "a":
        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                for k in range(len(possible_moves[i][j])):
                    possible_moves[i][j][k] = 7 - possible_moves[i][j][k]

    good_piece = 0
    for iter in range(1, 33):
        piece = np.argmax(predictions_piece)
        predictions_piece[piece] = -10
        x1 = math.floor(piece / 4)
        x2 = ((piece % 4) * 2 + 1) if x1 % 2 == 0 else ((piece % 4) * 2)
        select_piece = [x1, x2]
        it_found = False

        for possible_move in possible_moves:
            if possible_move[0][0] == select_piece[0] and possible_move[0][1] == select_piece[1]:
                it_found = True
                good_piece = piece
                break

        if it_found:
            break
        else:
            write_to_file_bad_piece(num_list, piece)
            if is_net_and_net == 1:
                count_of_bad_moves += 1

    piece_table = np.zeros((1, 32))
    piece_table[0, good_piece] = 1
    piece_table = piece_table.astype('float32')
    predictions_move = model_move.predict([piece_table, train_input])
    predictions_move = predictions_move[0]
    good_move = 0

    for iter in range(1, 33):
        move = np.argmax(predictions_move)
        predictions_move[move] = -10
        y1 = math.floor(move / 4)
        y2 = ((move % 4) * 2 + 1) if y1 % 2 == 0 else ((move % 4) * 2)
        it_found = False

        for possible_move in possible_moves:
            if possible_move[0][0] == x1 and possible_move[0][1] == x2 and possible_move[1][
                0] == y1 and possible_move[1][1] == y2:
                it_found = True
                good_move = move
                break

        if it_found:
            break
        else:
            write_to_file_bad_move(num_list, good_piece, move)
            if is_net_and_net == 1:
                count_of_bad_moves += 1

    return num_list, good_piece, good_move;


def get_rezult_from_rand(checkers):
    board_2 = copy.deepcopy(checkers.board)
    board_list = []

    if checkers.get_current_player() == "a":
        board_2.reverse()
        for i in range(len(board_2)):
            board_2[i].reverse()
        for i in range(len(board_2)):
            for j in range(len(board_2[i])):
                if board_2[i][j] == 'A':
                    board_2[i][j] = 'R'
                elif board_2[i][j] == 'a':
                    board_2[i][j] = 'r'
                elif board_2[i][j] == 'R':
                    board_2[i][j] = 'A'
                elif board_2[i][j] == 'r':
                    board_2[i][j] = 'a'

    for i in range(len(board_2)):
        for j in range(len(board_2[i])):
            if (i + j) % 2 == 0:
                continue
            element = board_2[i][j]
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

    possible_moves = checkers.get_possible_moves()

    if checkers.get_current_player() == "a":
        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                for k in range(len(possible_moves[i][j])):
                    possible_moves[i][j][k] = 7 - possible_moves[i][j][k]

    rand_move = possible_moves[random.randint(0, len(possible_moves) - 1)]

    good_piece = math.floor(rand_move[0][0] * 4 + rand_move[0][1] / 2)
    good_move = math.floor(rand_move[1][0] * 4 + rand_move[1][1] / 2)

    return num_list, good_piece, good_move;
