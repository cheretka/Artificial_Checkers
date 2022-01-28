from tensorflow import keras
from tensorflow.keras import layers
from Savery import *
import random
from main2 import *
import main2

def fit_piece_network_bad_choice():
    # board
    print(main2.data_p_faulty_board)
    print(main2.data_p_faulty_board.shape)
    rand_indexes = random.sample(range(len(main2.data_p_faulty_board) - 1), 2048)
    input_boards = []
    for index in rand_indexes:
        input_boards.append(main2.data_p_faulty_board[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    # piece
    data_pieces = load_smth_from_file("p_faulty_piece.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(data_pieces[index])

    # model
    output_pieces = main2.model_piece.predict(input_boards)

    for i in range(2048):
        output_pieces[i][train_pieces[i]] = -1

    main2.model_piece.fit(input_boards, y = output_pieces, batch_size = 32, epochs = 1, verbose = 0)


def fit_move_network_bad_choice():
    # board
    rand_indexes = random.sample(range(len(main2.data_m_faulty_board) - 1), 4096)
    input_boards = []
    for index in rand_indexes:
        input_boards.append(main2.data_m_faulty_board[index])
    input_boards = np.array(input_boards).astype('float32') / 5

    # piece
    input_pieces = np.zeros((4096, 32))
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(main2.data_m_faulty_piece[index])
    for i in range(4096):
        input_pieces[i][train_pieces[i]] = 1

    # move
    train_moves = []
    for index in rand_indexes:
        train_moves.append(main2.data_m_faulty_move[index])

    # model
    output_moves = main2.model_move.predict([input_boards, input_pieces])

    for i in range(4096):
        output_moves[i][train_moves[i]] = -1

    main2.model_move.fit([input_boards, input_pieces], y = output_moves, batch_size = 32,
                         epochs = 1, verbose = 0)


# ----------------------------------------------------------------------------------------------------------------------


def fit_piece_network_good_choice():
    # board 1
    rand_indexes = random.sample(range(len(main2.data_correct_board_1) - 1), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(main2.data_correct_board_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    # piece 1
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append(main2.data_correct_piece_1[index])

    # board 2
    boards_2 = []
    for index in rand_indexes:
        boards_2.append(main2.data_correct_board_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    # piece 2
    moves_2 = []
    for index in rand_indexes:
        moves_2.append(main2.data_correct_move_2[index])

    # models ----------------------------------------------
    predict_piece_1 = main2.model_piece.predict(boards_1)
    predict_piece_2 = main2.model_piece.predict(boards_2)

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

    main2.model_piece.fit(boards_1, y = predict_piece_1, batch_size = 32, epochs = 1, verbose = 0)


def fit_move_network_good_choice():
    # board 1
    rand_indexes = random.sample(range(len(main2.data_correct_board_1) - 1), 512)
    boards_1 = []
    for index in rand_indexes:
        boards_1.append(main2.data_correct_board_1[index])
    boards_1 = np.array(boards_1).astype('float32') / 5

    # piece 1
    input_pieces = np.zeros((512, 32))
    pieces_1 = []
    for index in rand_indexes:
        pieces_1.append(main2.data_correct_piece_1[index])
    for i in range(512):
        input_pieces[i][pieces_1[i]] = 1

    # move 1
    moves_1 = []
    for index in rand_indexes:
        moves_1.append(main2.data_correct_move_1[index])

    # board 2
    boards_2 = []
    for index in rand_indexes:
        boards_2.append(main2.data_correct_board_2[index])
    boards_2 = np.array(boards_2).astype('float32') / 5

    # piece 2
    piece_tables_2 = np.zeros((512, 32))
    pieces_2 = []
    for index in rand_indexes:
        pieces_2.append(main2.data_correct_piece_2[index])
    for i in range(512):
        piece_tables_2[i][pieces_2[i]] = 1

    # move 2
    moves_2 = []
    for index in rand_indexes:
        moves_2.append(main2.data_correct_move_2[index])

    # models -------------------------------------------------
    predict_move_1 = main2.model_move.predict([boards_1, input_pieces])
    predict_move_2 = main2.model_move.predict([boards_2, piece_tables_2])

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

    main2.model_move.fit([boards_1, input_pieces], y = predict_move_1, batch_size = 32, epochs = 1,
                         verbose = 0)
