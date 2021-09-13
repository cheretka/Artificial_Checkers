import random
from math import inf

def minimax(checkers, max_min, AI_letter, depth):
    someone_won = checkers.get_win()
    if someone_won == 'remis':
        return 0
    elif someone_won == AI_letter:
        return 100
    elif someone_won != AI_letter and someone_won is not None:
        return -100

    if depth == 0:
        a = 0
        r = 0
        for row in range(len(checkers.board)):
            for kolm in range(len(checkers.board[row])):
                if checkers.board[row][kolm] == 'A':
                    a = a + 3
                elif checkers.board[row][kolm] == 'a':
                    a = a + 1
                elif checkers.board[row][kolm] == 'R':
                    r = r + 3
                elif checkers.board[row][kolm] == 'r':
                    r = r + 1

        return (a - r) if AI_letter == 'a' else (r - a)


    scores = []
    possible_moves = checkers.get_possible_moves()
    score = 0
    for move in possible_moves:
        new_checkers = checkers.make_move(move)
        if checkers.get_current_player() == AI_letter:
            score = minimax(new_checkers, 1, AI_letter, depth-1)
        else:
            score = minimax(new_checkers, -1, AI_letter, depth-1)
        scores.append(score)

    return min(scores) if max_min == -1 else max(scores)




def select_move(board, diff):
    AI_letter = board.get_current_player()

    best_score = -inf
    best_moves = []

    possible_moves = board.get_possible_moves()
    if len(possible_moves) == 1:
        return_move = possible_moves[0]
        # print(AI_letter, ":  return_move ", return_move)
        return return_move


    for move in possible_moves:
        new_checkers = board.make_move(move)

        if board.get_current_player() == AI_letter:
            score = minimax(new_checkers, 1, AI_letter, diff)
        else:
            score = minimax(new_checkers, -1, AI_letter, diff)

        if score == best_score:
            best_moves.append(move)
        elif score > best_score:
            best_score = score
            best_moves = []
            best_moves.append(move)
        # print(move)

    # print("best_score: " + str(best_score) + "  final_move len: " + str(len(best_moves)))
    # print(best_moves)
    return random.choice(best_moves)



