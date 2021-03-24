import random


def alphabeta(checkers, isMax, AI_letter, depth, alpha, beta):
    someone_won = checkers.get_win()
    if someone_won == AI_letter:
        return 24
    elif someone_won != AI_letter and someone_won is not None:
        return -24

    if depth == 0:
        a = 0
        r = 0
        for row in range(len(checkers.board)):
            for kolm in range(len(checkers.board[row])):
                if checkers.board[row][kolm].lower() == 'a':
                    a = a + 1
                elif checkers.board[row][kolm].lower() == 'r':
                    r = r + 1

        if a > r:
            if AI_letter == 'a':
                return a
            else:
                return -r
        elif r > a:
            if AI_letter == 'r':
                return r
            else:
                return -a
        else:
            return 0

    scores = []
    possible_moves = checkers.get_possible_moves()
    score = 0
    for move in possible_moves:
        checkers.make_move(move)
        if checkers.whose_turn() == AI_letter:
            score = alphabeta(checkers, True, AI_letter, depth - 1, alpha, beta)
        else:
            score = alphabeta(checkers, False, AI_letter, depth - 1, alpha, beta)
        scores.append(score)
        checkers.undo_move()
        if isMax:
            alpha = max(alpha, score)
            if beta<=alpha:
                break
        else:
            beta = min(beta, score)
            if beta <= alpha:
                break

    return min(scores) if (isMax == False) else max(scores)







def get_move(board, diff):
    AI = board.whose_turn()
    # print(board.whose_turn())
    best_score = -1000
    final_move = []

    possible_moves = board.get_possible_moves()
    for move in possible_moves:
        board.make_move(move)
        if board.whose_turn() == AI:
            score = alphabeta(board, True, AI, diff, -1000, 1000)
        else:
            score = alphabeta(board, False, AI, diff, 1000, -1000)
        board.undo_move()

        if score == best_score:
            final_move.append(move)
        elif score > best_score:
            best_score = score
            final_move = []
            final_move.append(move)
        # print(move)

    print("best_score: " + str(best_score) + "  final_move len: " + str(len(final_move)))
    # print(final_move)
    return random.choice(final_move)
