from tensorflow import keras
from tensorflow.keras import layers
from Savery import *
import random


def fit_piece_network_bad_choice():
    # print("start - fit_piece_network_bad_choice")

    data_boards = load_board_from_file("p_faulty_board.txt")
    rand_indexes = random.sample(range(len(data_boards)), 4096)
    input_boards = []
    for index in rand_indexes:
        input_boards.append(data_boards[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    model_piece = keras.models.load_model("model_piece_3")
    output_pieces = model_piece.predict(input_boards)

    data_pieces = load_smth_from_file("p_faulty_piece.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(data_pieces[index])

    for i in range(4096):
        output_pieces[i][train_pieces[i]] = -1

    model_piece.fit(input_boards, y = output_pieces, batch_size = 32, epochs = 1, verbose = 0)

    model_piece.save("model_piece_3")


def fit_move_network_bad_choice():
    # print("start - fit_move_network_bad_choice")

    data_boards = load_board_from_file("m_faulty_board.txt")
    rand_indexes = random.sample(range(len(data_boards)), 4096)
    input_boards = []
    for index in rand_indexes:
        input_boards.append(data_boards[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    input_pieces = np.zeros((4096, 32))
    data_pieces = load_smth_from_file("m_faulty_piece.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(data_pieces[index])
    for i in range(4096):
        input_pieces[i][train_pieces[i]] = 1

    model_move = keras.models.load_model("model_move_3")
    output_moves = model_move.predict([input_boards, input_pieces])

    data_moves = load_smth_from_file("m_faulty_move.txt").astype('int')
    train_moves = []
    for index in rand_indexes:
        train_moves.append(data_moves[index])
    for i in range(4096):
        output_moves[i][train_moves[i]] = -1

    model_move.fit([input_boards, input_pieces], y = output_moves, batch_size = 32, epochs = 1,
                   verbose = 0)

    model_move.save("model_move_3")


# ----------------------------------------------------------------------------------------------------------------------


def fit_piece_network_good_choice():
    # print("start - fit_piece_network_good_choice")

    data_boards_1 = load_board_from_file("correct_board_1.txt")
    rand_indexes = random.sample(range(len(data_boards_1)), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(data_boards_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    model = keras.models.load_model("model_piece_3")
    predict_piece_1 = model.predict(boards_1)

    data_pieces_1 = load_smth_from_file("correct_piece_1.txt").astype('int')
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append(data_pieces_1[index])

    data_boards_2 = load_board_from_file("correct_board_2.txt")
    boards_2 = []
    for index in rand_indexes:
        boards_2.append(data_boards_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    predict_piece_2 = model.predict(boards_2)

    data_move_2 = load_smth_from_file("correct_move_2.txt").astype('int')
    moves_2 = []
    for index in rand_indexes:
        moves_2.append(data_move_2[index])

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
            maxim = max(predict_piece_2[i])
            predict_piece_1[i][pieces_1[i]] = ocena + 0.8 * maxim

    model.fit(boards_1, y = predict_piece_1, batch_size = 32, epochs = 1, verbose = 0)

    model.save("model_piece_3")


def fit_move_network_good_choice():
    # print("start - fit_piece_network_good_choice")

    data_boards_1 = load_board_from_file("correct_board_1.txt")
    rand_indexes = random.sample(range(len(data_boards_1)), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(data_boards_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    input_pieces = np.zeros((512, 32))
    data_pieces_1 = load_smth_from_file("correct_piece_1.txt").astype('int')
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append(data_pieces_1[index])
    for i in range(512):
        input_pieces[i][pieces_1[i]] = 1

    model = keras.models.load_model("model_move_3")
    predict_move_1 = model.predict([boards_1, input_pieces])

    data_moves_1 = load_smth_from_file("correct_move_1.txt").astype('int')
    moves_1 = []
    for index in rand_indexes:
        moves_1.append(data_moves_1[index])

    data_boards_2 = load_board_from_file("correct_board_2.txt")
    boards_2 = []
    for index in rand_indexes:
        boards_2.append(data_boards_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    piece_tables_2 = np.zeros((512, 32))
    data_pieces_2 = load_smth_from_file("correct_piece_2.txt").astype('int')
    pieces_2 = []
    for index in rand_indexes:
        pieces_2.append(data_pieces_2[index])
    for i in range(512):
        piece_tables_2[i][pieces_2[i]] = 1

    predict_move_2 = model.predict([boards_2, piece_tables_2])

    data_moves_2 = load_smth_from_file("correct_move_2.txt").astype('int')
    moves_2 = []
    for index in rand_indexes:
        moves_2.append(data_moves_2[index])

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
            maxim = max(predict_move_2[i])
            predict_move_1[i][moves_1[i]] = ocena + 0.8 * maxim

    model.fit([boards_1, input_pieces], y = predict_move_1, batch_size = 32, epochs = 1,
              verbose = 0)

    model.save("model_move_3")
