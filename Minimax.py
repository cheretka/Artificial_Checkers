import random


def minimax(checkers, max_min, AI_letter, depth):
    someone_won = checkers.get_win()
    if someone_won == AI_letter:
        return 13
    elif someone_won != AI_letter and someone_won is not None:
        return -13

    if depth == 0:
        a = 0
        r = 0
        for row in range(len(checkers.board)):
            for kolm in range(len(checkers.board[row])):
                if checkers.board[row][kolm].lower() == 'a':
                    a = a+1
                elif checkers.board[row][kolm].lower() == 'r':
                    r = r+1

        if a>r:
            if  AI_letter=='a':
                return a + (6-r)
            else:
                return -r + (12-a)
        elif r>a:
            if AI_letter == 'a':
                return r + (6 - a)
            else:
                return -a + (12 - r)
        else:
            return 0


    scores = []
    possible_moves = checkers.get_possible_moves()
    score = 0
    for move in possible_moves:
        checkers.make_move(move)
        if checkers.whose_turn() == AI_letter:
            score = minimax(checkers, 1, AI_letter, depth-1)
        else:
            score = minimax(checkers, -1, AI_letter, depth-1)
        scores.append(score)
        checkers.undo_move()


    return min(scores) if max_min == -1 else max(scores)




def get_move(board):
    AI = board.whose_turn()
    best_score = -1000
    final_move = []

    possible_moves = board.get_possible_moves()
    for move in possible_moves:
        board.make_move(move)
        if board.whose_turn() == AI:
            score = minimax(board, 1, AI, 11)
        else:
            score = minimax(board, -1, AI, 11)
        board.undo_move()

        if score == best_score:
            final_move.append(move)
        elif score > best_score:
            best_score = score
            final_move = []
            final_move.append(move)
        print(move)

    print("best_score: " + str(best_score) + "  final_move len: " + str(len(final_move)))
    print(final_move)
    return random.choice(final_move)




# def counting(checkers):
#     a = 0
#     r = 0
#     for row in range(len(checkers.board)):
#         for kolm in range(len(checkers.board[row])):
#             if checkers.board[row][kolm].lower() == 'a':
#                 a = a+1
#             elif checkers.board[row][kolm].lower() == 'r':
#                 r = r+1
#
#     if a > r:
#         return 'a'
#     elif r > a:
#         return 'r'
#     else:
#         return 0
