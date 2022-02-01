# from a_play_games import *
# from ab_fit_all_models import *
# import GetFromNetwork
import numpy as np
import math
# import a_play_games
from tensorflow import keras
from tensorflow.keras import layers
from Savery import *
import random
from Checkers_state import *

data_correct_board_1 = 0
data_correct_piece_1 = 0
data_correct_move_1 = 0
data_correct_board_2 = 0
data_correct_piece_2 = 0
data_correct_move_2 = 0

data_p_faulty_board = 0
data_p_faulty_piece = 0

data_m_faulty_board = 0
data_m_faulty_piece = 0
data_m_faulty_move = 0

model_piece = 0
model_move = 0

count_of_bad_moves = 0
count_of_good_moves = 0

def initialization():
    global data_correct_board_1
    global data_correct_piece_1
    global data_correct_move_1
    global data_correct_board_2
    global data_correct_piece_2
    global data_correct_move_2

    global data_p_faulty_board
    global data_p_faulty_piece

    global data_m_faulty_board
    global data_m_faulty_piece
    global data_m_faulty_move

    global model_piece
    global model_move

    # correct data
    data_correct_board_1 = np.loadtxt("correct_board_1.txt").reshape(-1, 32)
    data_correct_piece_1 = np.loadtxt("correct_piece_1.txt").astype('int')
    data_correct_move_1 = np.loadtxt("correct_move_1.txt").astype('int')
    data_correct_board_2 = np.loadtxt("correct_board_2.txt").reshape(-1, 32)
    data_correct_piece_2 = np.loadtxt("correct_piece_2.txt").astype('int')
    data_correct_move_2 = np.loadtxt("correct_move_2.txt").astype('int')
    # a_play_games.ile_good = len(data_correct_piece_1)

    # bad piece
    data_p_faulty_board = np.loadtxt("p_faulty_board.txt").reshape(-1, 32)
    # print(data_p_faulty_board.shape)
    data_p_faulty_piece = np.loadtxt("p_faulty_piece.txt").astype('int')
    # GetFromNetwork.ile_p_bad = len(data_p_faulty_piece)

    # bad move
    data_m_faulty_board = np.loadtxt("m_faulty_board.txt").reshape(-1, 32)
    data_m_faulty_piece = np.loadtxt("m_faulty_piece.txt").astype('int')
    data_m_faulty_move = np.loadtxt("m_faulty_move.txt").astype('int')
    # GetFromNetwork.ile_m_bad = len(data_m_faulty_piece)

    # models
    model_piece = keras.models.load_model("model_piece_3")
    model_move = keras.models.load_model("model_move_3")


def save_data():
    global data_correct_board_1
    global data_correct_piece_1
    global data_correct_move_1
    global data_correct_board_2
    global data_correct_piece_2
    global data_correct_move_2

    global data_p_faulty_board
    global data_p_faulty_piece

    global data_m_faulty_board
    global data_m_faulty_piece
    global data_m_faulty_move

    global model_piece
    global model_move

    # models
    model_piece.save("model_piece_3")
    model_move.save("model_move_3")

    # correct data
    file = open("correct_board_1.txt", "w")
    np.savetxt(file, data_correct_board_1)
    file.close()
    file = open("correct_piece_1.txt", "w")
    np.savetxt(file, data_correct_piece_1)
    file.close()
    file = open("correct_move_1.txt", "w")
    np.savetxt(file, data_correct_move_1)
    file.close()
    file = open("correct_board_2.txt", "w")
    np.savetxt(file, data_correct_board_2)
    file.close()
    file = open("correct_piece_2.txt", "w")
    np.savetxt(file, data_correct_piece_2)
    file.close()
    file = open("correct_move_2.txt", "w")
    np.savetxt(file, data_correct_move_2)
    file.close()

    # bad piece
    file = open("p_faulty_board.txt", "w")
    np.savetxt(file, data_p_faulty_board)
    file.close()
    file = open("p_faulty_piece.txt", "w")
    np.savetxt(file, data_p_faulty_piece)
    file.close()

    # bad move
    file = open("m_faulty_board.txt", "w")
    np.savetxt(file, data_m_faulty_board)
    file.close()
    file = open("m_faulty_piece.txt", "w")
    np.savetxt(file, data_m_faulty_piece)
    file.close()
    file = open("m_faulty_move.txt", "w")
    np.savetxt(file, data_m_faulty_move)
    file.close()


def fit_piece_network_bad_choice():
    global data_p_faulty_board
    global data_p_faulty_piece
    global model_piece

    # print(data_p_faulty_board)
    data_p_faulty_board = data_p_faulty_board.reshape(-1, 32)
    # print(data_p_faulty_board.shape)
    # print(data_p_faulty_piece.shape)
    
    # board
    rand_indexes = random.sample(range(len( data_p_faulty_piece) - 1), 1024)
    input_boards = []
    for index in rand_indexes:
        input_boards.append( data_p_faulty_board[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    # piece
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(data_p_faulty_piece[index])

    # model
    output_pieces = model_piece.predict(input_boards)

    for i in range(1024):
        output_pieces[i][train_pieces[i]] = -1

    model_piece.fit(input_boards, y = output_pieces, batch_size = 32, epochs = 1, verbose = 0)


def fit_move_network_bad_choice():
    global data_m_faulty_board
    global data_m_faulty_piece
    global data_m_faulty_move
    global model_move

    data_m_faulty_board = data_m_faulty_board.reshape(-1, 32)
    
    # board
    rand_indexes = random.sample(range(len(data_m_faulty_piece) - 1), 1024)
    input_boards = []
    for index in rand_indexes:
        input_boards.append(data_m_faulty_board[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    # piece
    input_pieces = np.zeros((1024, 32))
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append( data_m_faulty_piece[index])
    for i in range(1024):
        input_pieces[i][train_pieces[i]] = 1

    # move
    train_moves = []
    for index in rand_indexes:
        train_moves.append( data_m_faulty_move[index])

    # model
    output_moves = model_move.predict([input_boards, input_pieces])

    for i in range(1024):
        output_moves[i][train_moves[i]] = -1

    model_move.fit([input_boards, input_pieces], y = output_moves, batch_size = 32,
                         epochs = 1, verbose = 0)


def fit_piece_network_good_choice():
    global data_correct_board_1
    global data_correct_piece_1
    global data_correct_move_1
    global data_correct_board_2
    global data_correct_piece_2
    global data_correct_move_2
    global model_piece

    data_correct_board_1 = data_correct_board_1.reshape(-1, 32)
    data_correct_board_2 = data_correct_board_2.reshape(-1, 32)

    # board 1
    rand_indexes = random.sample(range(len(data_correct_piece_1) - 1), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(data_correct_board_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    # piece 1
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append( data_correct_piece_1[index])

    # board 2
    boards_2 = []
    for index in rand_indexes:
        boards_2.append( data_correct_board_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    # piece 2
    moves_2 = []
    for index in rand_indexes:
        moves_2.append( data_correct_move_2[index])

    # models ----------------------------------------------
    predict_piece_1 = model_piece.predict(boards_1)
    predict_piece_2 = model_piece.predict(boards_2)

    for i in range(512):
        if moves_2[i] == 100:
            predict_piece_1[i][pieces_1[i]] = 1
        elif moves_2[i] == -100:
            predict_piece_1[i][pieces_1[i]] = -1
        elif moves_2[i] == 50:
            predict_piece_1[i][pieces_1[i]] = 0
        else:
            suma = sum(boards_1[i]) - sum(boards_2[i])
            ocena = 0
            if suma > 0:
                ocena = -0.1
            elif suma < 0:
                ocena = 0.1
            predict_piece_1[i][pieces_1[i]] = ocena + 0.8 * max(predict_piece_2[i])

    model_piece.fit(boards_1, y = predict_piece_1, batch_size = 32, epochs = 1, verbose = 0)


def fit_move_network_good_choice():
    global data_correct_board_1
    global data_correct_piece_1
    global data_correct_move_1
    global data_correct_board_2
    global data_correct_piece_2
    global data_correct_move_2
    global model_move

    data_correct_board_1 = data_correct_board_1.reshape(-1, 32)
    data_correct_board_2 = data_correct_board_2.reshape(-1, 32)

    # board 1
    rand_indexes = random.sample(range(len(data_correct_piece_1) - 1), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(data_correct_board_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    # piece 1
    input_pieces = np.zeros((512, 32))
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append( data_correct_piece_1[index])
    for i in range(512):
        input_pieces[i][pieces_1[i]] = 1

    # move 1
    moves_1 = []
    for index in rand_indexes:
        moves_1.append( data_correct_move_1[index])

    # board 2
    boards_2 = []
    for index in rand_indexes:
        boards_2.append( data_correct_board_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    # piece 2
    piece_tables_2 = np.zeros((512, 32))
    pieces_2 = []
    for index in rand_indexes:
        pieces_2.append( data_correct_piece_2[index])
    for i in range(512):
        piece_tables_2[i][pieces_2[i]] = 1

    # move 2
    moves_2 = []
    for index in rand_indexes:
        moves_2.append( data_correct_move_2[index])

    # models -------------------------------------------------
    predict_move_1 = model_move.predict([boards_1, input_pieces])
    predict_move_2 = model_move.predict([boards_2, piece_tables_2])

    for i in range(512):
        if moves_2[i] == 100:
            predict_move_1[i][moves_1[i]] = 1
        elif moves_2[i] == -100:
            predict_move_1[i][moves_1[i]] = -1
        elif moves_2[i] == 50:
            predict_move_1[i][moves_1[i]] = 0
        else:
            suma = sum(boards_1[i]) - sum(boards_2[i])
            ocena = 0
            if suma > 0:
                ocena = -0.1
            elif suma < 0:
                ocena = 0.1
            predict_move_1[i][moves_1[i]] = ocena + 0.8 * max(predict_move_2[i])

    model_move.fit([boards_1, input_pieces], y = predict_move_1, batch_size = 32, epochs = 1,
                         verbose = 0)


def write_to_file(board_1, piece_1, move_1, board_2, piece_2, move_2):
    global data_correct_board_1
    global data_correct_piece_1
    global data_correct_move_1
    global data_correct_board_2
    global data_correct_piece_2
    global data_correct_move_2

    if len(data_correct_piece_1) >= 10000:

        data_correct_board_1 = np.delete(data_correct_board_1, range(3000), axis = 0)
        data_correct_piece_1 = np.delete(data_correct_piece_1, range(3000), axis = 0)
        data_correct_move_1 = np.delete(data_correct_move_1, range(3000), axis = 0)
        data_correct_board_2 = np.delete(data_correct_board_2, range(3000), axis = 0)
        data_correct_piece_2 = np.delete(data_correct_piece_2, range(3000), axis = 0)
        data_correct_move_2 = np.delete(data_correct_move_2, range(3000), axis = 0)

    data_correct_board_1 = np.append(data_correct_board_1, board_1).reshape(-1, 32)
    data_correct_piece_1 = np.append(data_correct_piece_1, piece_1)
    data_correct_move_1 = np.append(data_correct_move_1, move_1)
    data_correct_board_2 = np.append(data_correct_board_2, board_2).reshape(-1, 32)
    data_correct_piece_2 = np.append(data_correct_piece_2, piece_2)
    data_correct_move_2 = np.append(data_correct_move_2, move_2)


def check(network_move, all_moves):
    for move in all_moves:
        if move[0] == network_move[0] and move[1] == network_move[1]:
            return move
    return None


def play_game_and_write_moves():
    global model_piece
    global model_move
    global count_of_bad_moves
    global count_of_good_moves

    checkers = Checkers_state()
    r_board_1, r_piece_1, r_move_1, a_board_1, a_piece_1, a_move_1 = None, None, None, None, None, None

    while checkers.get_win() is None:

        out_board_2, out_piece_2, out_move_2 = get_rezult_from_network(checkers, 1)

        if checkers.get_current_player() == 'r':
            if r_board_1 is not None:
                write_to_file(r_board_1, r_piece_1, r_move_1, out_board_2, out_piece_2, out_move_2)

            r_board_1 = out_board_2
            r_piece_1 = out_piece_2
            r_move_1 = out_move_2

            x1 = math.floor(r_piece_1 / 4)
            x2 = ((r_piece_1 % 4) * 2 + 1) if x1 % 2 == 0 else ((r_piece_1 % 4) * 2)
            y1 = math.floor(r_move_1 / 4)
            y2 = ((r_move_1 % 4) * 2 + 1) if y1 % 2 == 0 else ((r_move_1 % 4) * 2)
            selected_move = [[x1, x2], [y1, y2]]

        else:
            if a_board_1 is not None:
                write_to_file(a_board_1, a_piece_1, a_move_1, out_board_2, out_piece_2, out_move_2)

            a_board_1 = out_board_2
            a_piece_1 = out_piece_2
            a_move_1 = out_move_2

            x1 = math.floor(a_piece_1 / 4)
            x2 = ((a_piece_1 % 4) * 2 + 1) if x1 % 2 == 0 else ((a_piece_1 % 4) * 2)
            y1 = math.floor(a_move_1 / 4)
            y2 = ((a_move_1 % 4) * 2 + 1) if y1 % 2 == 0 else ((a_move_1 % 4) * 2)
            selected_move = [[7 - x1, 7 - x2], [7 - y1, 7 - y2]]

        selected_move = check(selected_move, checkers.get_possible_moves())
        if selected_move is None:
            print("\n-------- the selected move is not possible -> MCTS  \n", "board\n",
                  checkers.current_player, checkers.board)
            checkers.printi()
            print("selected_move ", out_piece_2, "  ", out_move_2)
            for i in checkers.get_possible_moves():
                print(i)
            exit()

        checkers = checkers.make_move(selected_move)
        count_of_good_moves += 1

    board_2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    board_list = []

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

    if checkers.get_win() == 'r':
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, 100)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, -100)

    elif checkers.get_win() == 'a':
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, -100)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, 100)

    else:
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, 50)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, 50)


    print(count_of_bad_moves, " ", count_of_good_moves)
    f = open("results bad moves", "a+")
    f.write(str(count_of_bad_moves)+"\n")
    f.close()
    count_of_bad_moves = 0
    f = open("results good moves", "a+")
    f.write(str(count_of_good_moves) + "\n")
    f.close()
    count_of_good_moves = 0


def play_rand_game_and_write_moves():
    global model_piece
    global model_move

    checkers = Checkers_state()


    r_board_1 = None
    r_piece_1 = None
    r_move_1 = None

    a_board_1 = None
    a_piece_1 = None
    a_move_1 = None

    while checkers.get_win() is None:


        if checkers.get_current_player() == 'r':

            if random.randint(1, 2) == 1:
                r_board_2, r_piece_2, r_move_2 = get_rezult_from_rand(checkers)
            else:
                r_board_2, r_piece_2, r_move_2 = get_rezult_from_network(checkers, 0)

            if r_board_1 is not None:
                write_to_file(r_board_1, r_piece_1, r_move_1, r_board_2, r_piece_2,
                              r_move_2)

            r_board_1 = r_board_2
            r_piece_1 = r_piece_2
            r_move_1 = r_move_2

            x1 = math.floor(r_piece_2 / 4)
            x2 = ((r_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((r_piece_2 % 4) * 2)
            y1 = math.floor(r_move_2 / 4)
            y2 = ((r_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((r_move_2 % 4) * 2)
            selected_move = [[x1, x2], [y1, y2]]

        else:

            if random.randint(1, 2) == 1:
                a_board_2, a_piece_2, a_move_2 = get_rezult_from_rand(checkers)
            else:
                a_board_2, a_piece_2, a_move_2 = get_rezult_from_network(checkers, 0)

            if a_board_1 is not None:
                write_to_file(a_board_1, a_piece_1, a_move_1, a_board_2, a_piece_2,
                              a_move_2)

            a_board_1 = a_board_2
            a_piece_1 = a_piece_2
            a_move_1 = a_move_2

            x1 = math.floor(a_piece_2 / 4)
            x2 = ((a_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((a_piece_2 % 4) * 2)
            y1 = math.floor(a_move_2 / 4)
            y2 = ((a_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((a_move_2 % 4) * 2)

            selected_move = [[7 - x1, 7 - x2], [7 - y1, 7 - y2]]


        selected_move = check(selected_move, checkers.get_possible_moves())
        if selected_move is None:
            print("\n-------- the selected move is not possible -> MCTS  \n", "board\n", checkers.current_player)
            print(checkers.board)
            checkers.printi()
            print("selected_move ", selected_move)
            for i in checkers.get_possible_moves():
                print(i)
            exit()

        checkers = checkers.make_move(selected_move)

    board_2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    board_list = []

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

    if checkers.get_win() == 'r':
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, 100)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, -100)

    elif checkers.get_win() == 'a':
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, -100)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, 100)

    else:
        write_to_file(r_board_1, r_piece_1, r_move_1, num_list, 1, 50)
        write_to_file(a_board_1, a_piece_1, a_move_1, num_list, 1, 50)


def write_to_file_bad_piece(board, piece):
    global data_p_faulty_board
    global data_p_faulty_piece

    if len(data_p_faulty_piece) >= 100000:
        data_p_faulty_board = np.delete(data_p_faulty_board, range(30000), axis = 0)
        data_p_faulty_piece = np.delete(data_p_faulty_piece, range(30000), axis = 0)

    data_p_faulty_board = np.append(data_p_faulty_board, board).reshape(-1, 32)
    data_p_faulty_piece = np.append(data_p_faulty_piece, piece)


def write_to_file_bad_move(board, piece, move):
    global data_m_faulty_board
    global data_m_faulty_piece
    global data_m_faulty_move

    # print(data_m_faulty_piece)
    # print(data_m_faulty_piece.shape)
    if len(data_m_faulty_piece) >= 100000:
        data_m_faulty_board = np.delete(data_m_faulty_board, range(30000), axis = 0)
        data_m_faulty_piece = np.delete(data_m_faulty_piece, range(30000), axis = 0)
        data_m_faulty_move = np.delete(data_m_faulty_move, range(30000), axis = 0)

    data_m_faulty_board = np.append(data_m_faulty_board, board).reshape(-1, 32)
    data_m_faulty_piece = np.append(data_m_faulty_piece, piece)
    data_m_faulty_move = np.append(data_m_faulty_move, move)


def get_rezult_from_network(checkers, is_net_and_net):
    global count_of_bad_moves
    global model_piece
    global model_move

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
        predictions_piece[piece] = min(predictions_piece) - 1
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
        predictions_move[move] = min(predictions_move) - 1
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




if __name__ == "__main__":


    initialization()



    for i in range(1, 100000):

        # play
        play_rand_game_and_write_moves()

        # fit
        fit_piece_network_bad_choice()
        fit_move_network_bad_choice()
        fit_piece_network_good_choice()
        fit_move_network_good_choice()


        #  check
        if i % 10 == 0:
            play_game_and_write_moves()


        # save models and data to files
        if i % 100 == 0:
            save_data()
