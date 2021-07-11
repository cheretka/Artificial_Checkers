from Checkers_state import *
from Algorithms.MCTS import *
from MyNetwork import *


def check_move(network_move, all_moves):
    for move in all_moves:
        if move[0] == network_move[0] and move[1] == network_move[1]:
            return move

    return None


if __name__ == "__main__":
    print('Welcome to English draughts (checkers)!')

    checkers = Checkers_state()
    checkers.print()

    white_experience = 400

    while checkers.get_win() is None:

        selected_move = 0

        if checkers.get_current_player() == 'r':
            print("\n\nAI turn:")
            selected_move = get_move_from_network(checkers)
            print("selected move by AI ", selected_move)

            possible_moves = checkers.get_possible_moves()
            print("# possible moves for this board:")
            for move in possible_moves:
                print(move)

            selected_move = check_move(selected_move, possible_moves)
            if len(possible_moves) == 1:
                selected_move = possible_moves[0]
            elif selected_move == None:
                print("\n!! the selected move is not possible !!\n")
                break
        else:
            print("\n\nWhite turn:")
            # selecte move by MCTS
            selected_move = select_move(checkers, white_experience)

        checkers = checkers.make_move(selected_move)
        checkers.print(selected_move[0])

        print()

    if checkers.get_win() is not None:
        print("win: " + checkers.get_win())
