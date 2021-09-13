from NetworkMove import *
from NetworkPiece import *


def get_move_from_network(checkers):

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
    train_input = num_list.astype('float32') / 5

    train_input = np.reshape(train_input, (1, 32))
    # print("train_input ", type(train_input))
    # print(train_input.shape)
    # print(train_input)
    # print()



    model_piece = keras.models.load_model("model_piece")
    predictions_piece = model_piece.predict(train_input)
    model_piece.save("model_piece")

    piece = np.argmax(predictions_piece[0])

    piece_table = np.zeros((1, 32))
    piece_table[0, piece] = 1
    piece_table = piece_table.astype('float32')

    model_move = keras.models.load_model("model_move")
    predictions_move = model_move.predict([piece_table, train_input])
    model_move.save("model_move")

    move = np.argmax(predictions_move[0])




    # print("train_input ", type(predictions))
    # # print("shape ", predictions.shape)
    # print(predictions)
    # # print(sum(predictions[0]) )
    # # print()
    #
    # print("sum 0 ", sum(predictions[0][0]))
    # move = np.argmax(predictions[1])
    # print("sum 1 ", sum(predictions[1][0]))
    # print(piece, " ", move)
    #
    # for i in range(32):
    #     print(i, " ", predictions[1][0][i] * 100)


    x1 = math.floor(piece / 4)
    x2 = ((piece % 4) * 2 + 1) if x1 % 2 == 0 else ((piece % 4) * 2)
    y1 = math.floor(move / 4)
    y2 = ((move % 4) * 2 + 1) if y1 % 2 == 0 else ((move % 4) * 2)


    return [[x1, x2], [y1, y2]]
