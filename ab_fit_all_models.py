from tensorflow import keras
from tensorflow.keras import layers
from Savery import *
import random


def fit_piece_network_bad_choice():
    print("\nstart - fit_piece_network_bad_choice")

    boards = load_board_from_file("p_faulty_board.txt")
    rand_indexes = random.sample(range(len(boards)), 1024)
    train_input = []
    for index in rand_indexes:
        train_input.append(boards[index])
    train_input = np.array(train_input).astype('float32') / 5

    model = keras.models.load_model("model_piece_3")
    train_output_piece = model.predict(train_input)

    pieces = load_smth_from_file("p_faulty_piece.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(pieces[index])
    for i in range(1024):
        train_output_piece[i][train_pieces[i]] = -1

    history = model.fit(train_input,
                        y=train_output_piece,
                        batch_size=32,
                        epochs=1)

    model.save("model_piece_3")
    print("end - fit_piece_network_bad_choice\n")



def fit_move_network_bad_choice():
    print("\nstart - fit_move_network_bad_choice")

    boards = load_board_from_file("m_faulty_board.txt")
    rand_indexes = random.sample(range(len(boards)), 1024)
    train_input = []
    for index in rand_indexes:
        train_input.append(boards[index])
    train_input = np.array(train_input).astype('float32') / 5

    piece_tables = np.zeros((1024, 32))
    pieces = load_smth_from_file("m_faulty_piece.txt")
    pieces = pieces.astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(pieces[index])
    for i in range(len(piece_tables)):
        piece_tables[i][train_pieces[i]] = 1

    model = keras.models.load_model("model_move_3")
    train_output_move = model.predict([train_input, piece_tables])

    moves = load_smth_from_file("m_faulty_move.txt")
    moves = moves.astype('int')
    train_moves = []
    for index in rand_indexes:
        train_moves.append(moves[index])
    for i in range(len(train_output_move)):
        train_output_move[i][train_moves[i]] = -1

    history = model.fit([train_input, piece_tables],
                        y=train_output_move,
                        batch_size=32,
                        epochs=1)

    model.save("model_move_3")
    print("end - fit_move_network_bad_choice\n")


# ----------------------------------------------------------------------------------------------------------------------


def fit_piece_network_good_choice():
    print("\nstart - fit_piece_network_good_choice")

    boards = load_board_from_file("correct_board_1.txt")
    rand_indexes = random.sample(range(len(boards)), 128)
    train_input = []
    for index in rand_indexes:
        train_input.append(boards[index])
    train_input = np.array(train_input).astype('float32') / 5

    model = keras.models.load_model("model_piece_3")
    train_output_piece = model.predict(train_input)

    pieces = load_smth_from_file("correct_piece_1.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(pieces[index])

    boards_2 = load_board_from_file("correct_board_2.txt")
    train_input_2 = []
    for index in rand_indexes:
        train_input_2.append(boards_2[index])
    train_input_2 = np.array(train_input_2).astype('float32') / 5

    train_output_piece_2 = model.predict(train_input_2)

    pieces_2 = load_smth_from_file("correct_move_2.txt").astype('int')
    train_pieces_2 = []
    for index in rand_indexes:
        train_pieces_2.append(pieces_2[index])

    for i in range(len(rand_indexes)):
        if train_pieces_2[i] == 100:
            train_output_piece[i][train_pieces[i]] = 1
        elif train_pieces_2[i] == -100:
            train_output_piece[i][train_pieces[i]] = -1
        elif train_pieces_2[i] == 50:
            train_output_piece[i][train_pieces[i]] = 0
        else:
            suma = sum(train_input[i]) - sum(train_input_2[i])
            ocena = 0
            if suma > 0:
                ocena = -0.1
            elif suma < 0:
                ocena = 0.1
            maxim = max(train_output_piece_2[i])
            train_output_piece[i][train_pieces[i]] = ocena + 0.8 * maxim

    history = model.fit(train_input,
                        y=train_output_piece,
                        batch_size=32,
                        epochs=1)

    model.save("model_piece_3")
    print("end - fit_piece_network_good_choice\n")


def fit_move_network_good_choice():
    print("\nstart - fit_piece_network_good_choice")

    boards = load_board_from_file("correct_board_1.txt")
    rand_indexes = random.sample(range(len(boards)), 128)
    train_input = []
    for index in rand_indexes:
        train_input.append(boards[index])
    train_input = np.array(train_input).astype('float32') / 5

    piece_tables = np.zeros((128, 32))
    pieces = load_smth_from_file("correct_piece_1.txt").astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(pieces[index])
    for i in range(len(piece_tables)):
        piece_tables[i][train_pieces[i]] = 1

    model = keras.models.load_model("model_move_3")
    train_output_piece = model.predict(train_input, piece_tables)

    moves = load_smth_from_file("correct_move_1.txt").astype('int')
    train_moves = []
    for index in rand_indexes:
        train_moves.append(moves[index])

    boards_2 = load_board_from_file("correct_board_2.txt")
    train_input_2 = []
    for index in rand_indexes:
        train_input_2.append(boards_2[index])
    train_input_2 = np.array(train_input_2).astype('float32') / 5

    piece_tables_2 = np.zeros((128, 32))
    pieces = load_smth_from_file("correct_piece_2.txt")
    pieces = pieces.astype('int')
    train_pieces = []
    for index in rand_indexes:
        train_pieces.append(pieces[index])
    for i in range(len(piece_tables)):
        piece_tables_2[i][train_pieces[i]] = 1

    train_output_piece_2 = model.predict(train_input_2, piece_tables_2)

    moves_2 = load_smth_from_file("correct_move_2.txt").astype('int')
    train_moves_2 = []
    for index in rand_indexes:
        train_moves_2.append(moves_2[index])

    for i in range(len(rand_indexes)):
        if train_moves_2[i] == 100:
            train_output_piece[i][train_moves[i]] = 1
        elif train_moves_2[i] == -100:
            train_output_piece[i][train_moves[i]] = -1
        elif train_moves_2[i] == 50:
            train_output_piece[i][train_moves[i]] = 0
        else:
            suma = sum(train_input[i]) - sum(train_input_2[i])
            ocena = 0
            if suma > 0:
                ocena = -0.1
            elif suma < 0:
                ocena = 0.1
            maxim = max(train_output_piece_2[i])
            train_output_piece[i][train_moves[i]] = ocena + 0.8 * maxim

    history = model.fit([train_input, piece_tables],
                        y=train_output_piece,
                        batch_size=32,
                        epochs=1)

    model.save("model_piece_3")
    print("end - fit_piece_network_good_choice\n")
