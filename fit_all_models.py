from tensorflow import keras
from tensorflow.keras import layers
from Savery import *



def fit_piece_network_bad_choice():
    print("\nstart - fit_piece_network_bad_choice")

    model = keras.models.load_model("model_piece_3")


    print("## Load and reshape input/output data:")

    boards = load_board_from_file("p_faulty_board.txt")
    train_input = boards.astype('float32') / 5
    print("train_input ", train_input)
    print("shape ", train_input.shape)
    # print()


    train_output_piece = model.predict(train_input)
    # print("predictions ", train_output_piece)
    # print("predictions ", train_output_piece.shape)

    pieces = load_smth_from_file("p_faulty_piece.txt")
    pieces = pieces.astype('int')
    # print("pieces ", pieces)
    # print("pieces ", pieces.shape)

    for i in range(len(pieces)):
        train_output_piece[i][pieces[i]] = -1

    print("train_output_piece ", train_output_piece)
    print("shape ", train_output_piece.shape)
    # print()


    print('## Train the model on train_data')
    history = model.fit(train_input,
                        y=train_output_piece,
                        batch_size=32,
                        epochs=1)


    print('history dict:', history.history)

    model.save("model_piece_3")

    print("end - fit_piece_network_bad_choice\n")



def fit_piece_network_good_choice():

    model = keras.models.load_model("model_piece_3")


    print("\n## Load and reshape input/output data:")
    sample = 16
    number_of_games = 16

    train_input = load_board(sample, number_of_games)
    train_input = train_input.astype('float32') / 5
    print("train_input ", train_input)
    print("shape ", train_input.shape)
    print()


    train_output_piece = load_piece(sample, number_of_games)
    train_output_piece = train_output_piece.astype('float32')
    print("train_output_piece ", train_output_piece)
    print("shape ", train_output_piece.shape)
    print()



    print('\n## Train the model on train_data')
    # history = model.fit(train_input,
    #                     y=[train_output_piece, train_output_move],
    #                     batch_size=32,
    #                     epochs=200,
    #                     validation_data=(validation_input, [validation_output_piece, validation_output_move]))
    history = model.fit(train_input,
                        y=train_output_piece,
                        batch_size=32,
                        epochs=40)



    print('\nhistory dict:', history.history)

    model.save("model_piece_3")
    print("end - out fit_network")





def fit_move_network_bad_choice():
    print("\nstart - fit_move_network_bad_choice")

    model = keras.models.load_model("model_move_3")


    print("## Load and reshape input/output data:")

    boards = load_board_from_file("m_faulty_board.txt")
    train_input = boards.astype('float32') / 5
    print("train_input ", train_input)
    print("shape ", train_input.shape)
    # print()

    piece_tables = np.zeros((len(train_input), 32))
    pieces = load_smth_from_file("m_faulty_piece.txt")
    pieces = pieces.astype('int')
    print("pieces ", pieces)
    print("shape ", pieces.shape)

    for i in range(len(pieces)):
        piece_tables[i][pieces[i]] = 1


    train_output_move = model.predict([train_input, piece_tables])


    for i in range(len(pieces)):
        train_output_move[i][pieces[i]] = -1

    print("train_output_move ", train_output_move)
    print("shape ", train_output_move.shape)



    print('## Train the model on train_data')
    history = model.fit([train_input, piece_tables],
                        y=train_output_move,
                        batch_size=32,
                        epochs=1)


    print('history dict:', history.history)

    model.save("model_move_3")

    print("end - fit_move_network_bad_choice\n")