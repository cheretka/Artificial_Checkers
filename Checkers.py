import sys
import copy



class Checkers:

    def __init__(self):
        self.board = [[' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
                      ['r', ' ', 'r', ' ', 'r', ' ', 'r', ' '],
                      [' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['a', ' ', 'a', ' ', 'a', ' ', 'a', ' '],
                      [' ', 'a', ' ', 'a', ' ', 'a', ' ', 'a'],
                      ['a', ' ', 'a', ' ', 'a', ' ', 'a', ' ']]
        # self.board = [[' ', 'r', ' ', 'r', ' ', 'r'],
        #               ['r', ' ', 'r', ' ', 'r', ' '],
        #               [' ', ' ', ' ', ' ', ' ', ' '],
        #               [' ', ' ', ' ', ' ', ' ', ' '],
        #               [' ', 'a', ' ', 'a', ' ', 'a'],
        #               ['a', ' ', 'a', ' ', 'a', ' ']]
        self.length = 8
        self.stack = []
        self.current_player = "r"
        self.list_multi_jump = []




    def switch_player(self):
        self.current_player = 'a' if self.current_player == 'r' else 'r'




    def print(self):
        print()
        print("       0     1     2     3     4     5     6     7")
        print()
        print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        for row in range(8):
            sys.stdout.write("{}   |".format(row))
            for col in range(8):
                sys.stdout.write("  {}  |".format(self.board[row][col]))
            print()
            print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        print()
        # print("       0     1     2     3     4     5 ")

    # def print(self):
    #     print()
    #     print("       0     1     2     3     4     5  ")
    #     print()
    #     print("    +-----+-----+-----+-----+-----+-----+")
    #     for row in range(self.length):
    #         sys.stdout.write("{}   |".format(row))
    #         for col in range(self.length):
    #             sys.stdout.write("  {}  |".format(self.board[row][col]))
    #         print()
    #         print("    +-----+-----+-----+-----+-----+-----+")
    #     print()
    #     # print("       0     1     2     3     4     5     6     7")




    def get_win(self):
        if len(self.get_possible_moves()) == 0:
            return 'a' if self.current_player == 'r' else 'r'
        return None





    def make_move(self, move):
        self.stack.append([copy.deepcopy(self.board), self.whose_turn()])
        start_x = move[0][0]
        start_y = move[0][1]
        end_x = move[1][0]
        end_y = move[1][1]
        self.list_multi_jump = []
        self.board[end_x][end_y] = self.board[start_x][start_y]

        if (end_x == (self.length-1) and self.board[end_x][end_y] == 'r') or (end_x == 0 and self.board[end_x][end_y] == 'a'):
            self.board[end_x][end_y] = self.board[end_x][end_y].upper()
        self.board[start_x][start_y] = ' '

        if abs(end_x - start_x) == 2:
            self.board[(end_x + start_x) // 2][(end_y + start_y) // 2] = ' '
            if self.board[end_x][end_y].islower():
                self.list_multi_jump = self.get_possible_multi_jump_moves(end_x, end_y)
                if len(self.list_multi_jump) > 0:
                    self.switch_player()

        self.switch_player()





    def undo_move(self):
        self.board, self.current_player = self.stack.pop()





    def get_possible_moves(self):
        if len(self.list_multi_jump) > 0:
            return self.list_multi_jump

        other_player = 'a' if self.current_player == 'r' else 'r'
        delta = [[-1, -1], [-1, 1], [1, -1], [1, 1]] if self.current_player == 'a' else [[1, -1], [1, 1], [-1, -1], [-1, 1]]

        list_simple_moves = []
        list_jump_moves = []
        for row in range(len(self.board)):
            for kolm in range(len(self.board[row])):
                if self.board[row][kolm].lower() == self.current_player:
                    for index in range(4):
                        if self.board[row][kolm].islower() and index>1:
                            continue
                        new_row = row + delta[index][0]
                        new_kolm = kolm + delta[index][1]
                        if 0 <= new_row < len(self.board) and 0 <= new_kolm < len(self.board[row]):
                            if self.board[new_row][new_kolm] == ' ':
                                list_simple_moves.append([[row, kolm], [new_row, new_kolm]])
                            elif self.board[new_row][new_kolm].lower() == other_player:
                                new_row = new_row + delta[index][0]
                                new_kolm = new_kolm + delta[index][1]
                                if 0 <= new_row < len(self.board) and 0 <= new_kolm < len(self.board[row]) and self.board[new_row][new_kolm]== ' ':
                                    list_jump_moves.append([[row, kolm], [new_row, new_kolm]])

        if len(list_jump_moves) > 0:
            return list_jump_moves
        else:
            return list_simple_moves





    def get_possible_multi_jump_moves(self, row, kolm):
        other_player = 'a' if self.current_player == 'r' else 'r'
        delta = [[-1, -1], [-1, 1], [1, -1], [1, 1]] if self.current_player == 'a' else [[1, -1], [1, 1], [-1, -1], [-1, 1]]
        list_jump_moves = []

        for index in range(4):
            if self.board[row][kolm].islower() and index>1:
                continue
            new_row = row + delta[index][0]
            new_kolm = kolm + delta[index][1]
            if 0 <= new_row < len(self.board) and 0 <= new_kolm < len(self.board[row]) and self.board[new_row][new_kolm].lower() == other_player:
                    new_row = new_row + delta[index][0]
                    new_kolm = new_kolm + delta[index][1]
                    if 0 <= new_row < len(self.board) and 0 <= new_kolm < len(self.board[row]) and self.board[new_row][new_kolm]== ' ':
                        list_jump_moves.append([[row, kolm], [new_row, new_kolm]])

        return list_jump_moves






    def whose_turn(self):
        return self.current_player
