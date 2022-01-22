from NetworkMove import *
from NetworkPiece import *
import copy
from main2 import *

count_of_bad_moves = 0


def get_count_of_bad_moves():
    global count_of_bad_moves
    return count_of_bad_moves

def zero_count_of_bad_moves():
    global count_of_bad_moves
    count_of_bad_moves = 0
    return count_of_bad_moves


def write_to_file_bad_piece(board, piece):
    save_board_to_file(board, "p_faulty_board.txt")
    save_smth_to_file(piece, "p_faulty_piece.txt")


def write_to_file_bad_move(board, piece, move):
    save_board_to_file(board, "m_faulty_board.txt")
    save_smth_to_file(piece, "m_faulty_piece.txt")
    save_smth_to_file(move, "m_faulty_move.txt")


def get_rezult_from_network(checkers):
    global count_of_bad_moves
    # checkers_copy = Checkers_state()

    # print("\n---- get_rezult_from_network-----")
    board_2 = copy.deepcopy(checkers.board)
    # board_2 = [row[:] for row in checkers.board]
    # checkers.print()
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

    # print("board_list2", board_list)
    num_list = np.array(board_list)
    train_input = num_list.astype('float32') / 5

    train_input = np.reshape(train_input, (1, 32))

    model_piece = keras.models.load_model("model_piece_3")
    predictions_piece = model_piece.predict(train_input)
    predictions_piece = predictions_piece[0]
    # print("predictions_piece: ", predictions_piece)
    model_piece.save("model_piece_3")

    possible_moves = checkers.get_possible_moves()

    if checkers.get_current_player() == "a":

        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                for k in range(len(possible_moves[i][j])):
                    possible_moves[i][j][k] = 7 - possible_moves[i][j][k]

    good_piece = 0
    for iter in range(1, 33):
        piece = np.argmax(predictions_piece)
        # print("check if piece is ok ", iter, "predictions_piece: ", predictions_piece, "piece: ", piece)

        predictions_piece[piece] = -1

        x1 = math.floor(piece / 4)
        x2 = ((piece % 4) * 2 + 1) if x1 % 2 == 0 else ((piece % 4) * 2)

        select_piece = [x1, x2]
        it_found = False

        # print("select_piece ", select_piece)

        for possible_move in possible_moves:
            # print("possible_move ", possible_move)
            if possible_move[0][0] == select_piece[0] and possible_move[0][1] == select_piece[1]:
                # print("good selected piece: ", select_piece, "\n")
                it_found = True
                good_piece = piece
                break

        if it_found:
            break
        else:
            write_to_file_bad_piece(num_list, piece)
            count_of_bad_moves += 1
            # print(".")

    # x1 = math.floor(good_piece / 4)
    # x2 = ((good_piece % 4) * 2 + 1) if x1 % 2 == 0 else ((good_piece % 4) * 2)

    piece_table = np.zeros((1, 32))
    piece_table[0, good_piece] = 1
    # print("piece_table: ", piece_table)
    piece_table = piece_table.astype('float32')

    model_move = keras.models.load_model("model_move_3")
    predictions_move = model_move.predict([piece_table, train_input])
    predictions_move = predictions_move[0]
    # print("predictions_move: ", predictions_move)
    model_move.save("model_move_3")

    good_move = 0

    for iter in range(1, 33):

        move = np.argmax(predictions_move)
        # print("check if move is ok ", iter, "predictions_move: ", predictions_move, "move: ", move)

        predictions_move[move] = -1

        y1 = math.floor(move / 4)
        y2 = ((move % 4) * 2 + 1) if y1 % 2 == 0 else ((move % 4) * 2)

        select_move = [y1, y2]
        it_found = False

        for possible_move in possible_moves:
            if possible_move[0][0] == x1 and possible_move[0][1] == x2 and possible_move[1][0] == y1 and \
                    possible_move[1][1] == y2:
                # print("good selected move: ", select_move, "\n")
                it_found = True
                good_move = move
                break

        if it_found:
            break
        else:
            write_to_file_bad_move(num_list, good_piece, move)
            count_of_bad_moves += 1
            # print(".")

    # y1 = math.floor(good_move / 4)
    # y2 = ((good_move % 4) * 2 + 1) if y1 % 2 == 0 else ((good_move % 4) * 2)

    # if checkers.get_current_player() == "a":
    #     x1 = 7 - x1
    #     x2 = 7 - x2
    #     y1 = 7 - y1
    #     y2 = 7 - y2

    # return [[x1, x2], [y1, y2]]
    return num_list, good_piece, good_move;



def get_rezult_from_rand(checkers):

    # checkers_copy = Checkers_state()

    # print("\n---- get_rezult_from_network-----")
    board_2 = copy.deepcopy(checkers.board)
    # board_2 = [row[:] for row in checkers.board]
    # checkers.print()
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

    # print("board_list2", board_list)
    num_list = np.array(board_list)


    possible_moves = checkers.get_possible_moves()

    if checkers.get_current_player() == "a":

        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                for k in range(len(possible_moves[i][j])):
                    possible_moves[i][j][k] = 7 - possible_moves[i][j][k]


    rand_move = possible_moves[random.randint(0, len(possible_moves)-1)]
    print("rand_move ", rand_move)

    good_piece = math.floor(rand_move[0][0] * 4 + rand_move[0][1] / 2)
    print("good_piece ", good_piece)
    good_move = math.floor(rand_move[1][0] * 4 + rand_move[1][1] / 2)
    print("good_move ", good_move)




    return num_list, good_piece, good_move;
