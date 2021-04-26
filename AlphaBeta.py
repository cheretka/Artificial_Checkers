import random


def alphabeta(checkers, isMax, AI_letter, depth, alpha, beta):
    someone_won = checkers.get_win()
    if someone_won == 'm':
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
                    a = a + 2
                elif checkers.board[row][kolm] == 'a':
                    a = a + 1
                elif checkers.board[row][kolm] == 'R':
                    r = r + 2
                elif checkers.board[row][kolm] == 'r':
                    r = r + 1

        if AI_letter == 'a':
            if a > r:
                return a - r
            else:
                return - r + a
        else:
            if r > a:
                return r - a
            else:
                return -a + r


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
            if beta <= alpha or alpha==100:
                break
        else:
            beta = min(beta, score)
            if beta <= alpha or beta==-100:
                break

    return min(scores) if (isMax == False) else max(scores)







def get_move(board, diff):
    AI = board.whose_turn()
    print(board.whose_turn())
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


    print("best_score: " + str(best_score) + "  final_move len: " + str(len(final_move)))
    print(final_move)
    return random.choice(final_move)
