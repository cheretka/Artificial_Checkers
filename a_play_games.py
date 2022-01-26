from Checkers_state import *
import time
from GetFromNetwork import *
from Savery import *
from main2 import *
import random


ile_good = 0


def write_to_file(board_1, piece_1, move_1, board_2, piece_2, move_2):
    global ile_good

    if ile_good >= 10000:
        data_from_file = np.loadtxt("correct_piece_1.txt")
        file = open("correct_piece_1.txt", "w")
        np.savetxt(file, data_from_file[3000:])
        file.close()

        data_from_file = np.loadtxt("correct_piece_2.txt")
        file = open("correct_piece_2.txt", "w")
        np.savetxt(file, data_from_file[3000:])
        file.close()

        data_from_file = np.loadtxt("correct_move_1.txt")
        file = open("correct_move_1.txt", "w")
        np.savetxt(file, data_from_file[3000:])
        file.close()

        data_from_file = np.loadtxt("correct_move_2.txt")
        file = open("correct_move_2.txt", "w")
        np.savetxt(file, data_from_file[3000:])
        file.close()

        data_from_file = np.loadtxt("correct_board_1.txt")
        file = open("correct_board_1.txt", "w")
        np.savetxt(file, data_from_file[(32 * 3000):])
        file.close()

        data_from_file = np.loadtxt("correct_board_2.txt")
        file = open("correct_board_2.txt", "w")
        np.savetxt(file, data_from_file[(32 * 3000):])
        file.close()

        ile_good -= 3000

    save_board_to_file(board_1, "correct_board_1.txt")
    save_smth_to_file(piece_1, "correct_piece_1.txt")
    save_smth_to_file(move_1, "correct_move_1.txt")
    save_board_to_file(board_2, "correct_board_2.txt")
    save_smth_to_file(piece_2, "correct_piece_2.txt")
    save_smth_to_file(piece_2, "correct_move_2.txt")

    ile_good += 1


def check(network_move, all_moves):
    for move in all_moves:
        if move[0] == network_move[0] and move[1] == network_move[1]:
            return move

    return None


def play_game_and_write_moves():
    # print("   PART 1_2    start   play_game_and_write_moves")

    model_piece = keras.models.load_model("model_piece_3")
    model_move = keras.models.load_model("model_move_3")

    for i in range(1):

        checkers = Checkers_state()

        r_board_1 = None
        r_piece_1 = None
        r_move_1 = None

        a_board_1 = None
        a_piece_1 = None
        a_move_1 = None

        while checkers.get_win() is None:

            if checkers.get_current_player() == 'r':

                r_board_2, r_piece_2, r_move_2 = get_rezult_from_network(checkers, model_piece,
                                                                         model_move, 1)

                if r_board_1 is not None:
                    write_to_file(r_board_1, r_piece_1, r_move_1, r_board_2, r_piece_2,
                                  r_move_2)  # print(r_move_2)

                r_board_1 = r_board_2
                r_piece_1 = r_piece_2
                r_move_1 = r_move_2

                x1 = math.floor(r_piece_2 / 4)
                x2 = ((r_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((r_piece_2 % 4) * 2)
                y1 = math.floor(r_move_2 / 4)
                y2 = ((r_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((r_move_2 % 4) * 2)
                selected_move = [[x1, x2], [y1, y2]]

            else:

                a_board_2, a_piece_2, a_move_2 = get_rezult_from_network(checkers, model_piece,
                                                                         model_move, 1)

                if a_board_1 is not None:
                    write_to_file(a_board_1, a_piece_1, a_move_1, a_board_2, a_piece_2, a_move_2)

                a_board_1 = a_board_2
                a_piece_1 = a_piece_2
                a_move_1 = a_move_2

                x1 = math.floor(a_piece_2 / 4)
                x2 = ((a_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((a_piece_2 % 4) * 2)
                y1 = math.floor(a_move_2 / 4)
                y2 = ((a_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((a_move_2 % 4) * 2)
                # selected_move1 = [[x1, x2], [y1, y2]]
                selected_move = [[7 - x1, 7 - x2], [7 - y1, 7 - y2]]

                # print("selected_move ", selected_move)
            selected_move = check(selected_move, checkers.get_possible_moves())
            if selected_move is None:
                print("\n-------- the selected move is not possible -> MCTS  ")
                print("board")
                print(checkers.current_player)
                print(checkers.board)
                # checkers.print()
                print("selected_move ", selected_move)
                for i in checkers.get_possible_moves():
                    print(i)
                exit()

            checkers = checkers.make_move(selected_move)  # checkers.print(selected_move[0])

        board_2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

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

    # print("\n----------------------------------------------------------------------")
    print(get_count_of_bad_moves())
    zero_count_of_bad_moves()  # print("zero_count_of_bad_moves ", zero_count_of_bad_moves())  # print("         PART 1     end ")


def play_rand_game_and_write_moves():
    # print("        PART 1_2    start   play_rand_game_and_write_moves")

    model_piece = keras.models.load_model("model_piece_3")
    model_move = keras.models.load_model("model_move_3")

    for i in range(1):

        checkers = Checkers_state()
        # checkers.print()

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
                    # r_board_2, r_piece_2, r_move_2 = get_rezult_from_rand(checkers)
                    r_board_2, r_piece_2, r_move_2 = get_rezult_from_network(checkers, model_piece,
                                                                             model_move, 0)

                if r_board_1 is not None:
                    write_to_file(r_board_1, r_piece_1, r_move_1, r_board_2, r_piece_2,
                                  r_move_2)  # print(r_move_2)

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
                    a_board_2, a_piece_2, a_move_2 = get_rezult_from_network(checkers, model_piece,
                                                                             model_move, 0)

                if a_board_1 is not None:
                    write_to_file(a_board_1, a_piece_1, a_move_1, a_board_2, a_piece_2,
                                  a_move_2)  # print(a_move_2)

                a_board_1 = a_board_2
                a_piece_1 = a_piece_2
                a_move_1 = a_move_2

                x1 = math.floor(a_piece_2 / 4)
                x2 = ((a_piece_2 % 4) * 2 + 1) if x1 % 2 == 0 else ((a_piece_2 % 4) * 2)
                y1 = math.floor(a_move_2 / 4)
                y2 = ((a_move_2 % 4) * 2 + 1) if y1 % 2 == 0 else ((a_move_2 % 4) * 2)
                # selected_move1 = [[x1, x2], [y1, y2]]
                selected_move = [[7 - x1, 7 - x2], [7 - y1, 7 - y2]]

                # print("selected_move ", selected_move)
            selected_move = check(selected_move, checkers.get_possible_moves())
            if selected_move is None:
                print("\n-------- the selected move is not possible -> MCTS  ")
                print("board")
                print(checkers.current_player)
                print(checkers.board)
                # checkers.print()
                print("selected_move ", selected_move)
                for i in checkers.get_possible_moves():
                    print(i)
                exit()

            checkers = checkers.make_move(selected_move)  # checkers.print(selected_move[0])

        board_2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

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

    # print("\n----------------------------------------------------------------------")  # print("         PART 1_2     end ")
