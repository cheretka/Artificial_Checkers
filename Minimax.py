def minimax(board, max_min, AI_letter, depth):
    if depth==0:
        someone_won = board.get_win()
        if someone_won is None:
            else_won = counting(board)
            if else_won == AI_letter:
                return 1
            elif else_won != AI_letter and else_won !=0:
                return -1
            else:
                return 0

    someone_won = board.get_win()
    if someone_won == AI_letter:
        return 1
    elif someone_won != AI_letter and someone_won is not None:
        return -1



    scores = []
    possible_moves, order = board.get_possible_moves()
    score = 0
    for move in possible_moves:
        board.make_move(move)
        # board.print()
        if board.whose_turn() == AI_letter:
            score = minimax(board, 1, AI_letter, depth-1)
        else:
            score = minimax(board, -1, AI_letter, depth-1)
        scores.append(score)
        board.undo_move()
        # board.print()

    return min(scores) if max_min == -1 else max(scores)


def get_move(board):
    AI = board.whose_turn()
    best_score, final_move = -10, -1

    possible_moves, order = board.get_possible_moves()
    for move in possible_moves:
        board.make_move(move)
        # board.print()
        if board.whose_turn() == AI:
            score = minimax(board, 1, AI, 14)
        else:
            score = minimax(board, -1, AI, 14)
        board.undo_move()
        # board.print()
        if score > best_score:
            best_score, final_move = score, move

    return final_move

def counting(board):
    a = 0
    r = 0
    for row in range(len(board.values)):
        for kolm in range(len(board.values[row])):
            if board.values[row][kolm].lower() == 'a':
                a = a+1
            elif board.values[row][kolm].lower() == 'r':
                r = r+1

    if a > r:
        return 'a'
    elif r > a:
        return 'r'
    else:
        return 0
