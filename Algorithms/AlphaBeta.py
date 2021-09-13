import random
from math import inf

def alphabeta(checkers, AI_letter, depth, alpha, beta, maximizingPlayer):
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



    if maximizingPlayer:
        maxEval = -inf

        possible_moves = checkers.get_possible_moves()

        for move in possible_moves:
            new_checkers = checkers.make_move(move)
            eval = alphabeta(new_checkers, AI_letter, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            if beta <= alpha:
                break

        return maxEval

    else:

        minEval = inf

        possible_moves = checkers.get_possible_moves()

        for move in possible_moves:
            new_checkers = checkers.make_move(move)
            eval = alphabeta(new_checkers, AI_letter, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            if beta <= alpha:
                break

        return minEval





def select_move(board, depth):
    AI_letter = board.get_current_player()

    best_score = -inf
    best_moves = []

    possible_moves = board.get_possible_moves()
    if len(possible_moves) == 1:
        return_move = possible_moves[0]
        # print(AI_letter, ":  return_move ", return_move)
        return return_move


    for move in possible_moves:
        # print(move)
        new_checkers = board.make_move(move)
        eval = alphabeta(new_checkers, AI_letter, depth, -inf, inf, False)
        if eval == best_score:
            best_moves.append(move)
        if eval > best_score:
            best_score = eval
            best_moves = []
            best_moves.append(move)


    return_move = random.choice(best_moves)
    # print(AI_letter, ":  best_score: ", str(best_score), "  len: ", str(len(best_moves)), "return_move ", return_move)
    return return_move
