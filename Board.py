import sys
from piece import *
import copy

class Board:

    def __init__(self):
        # self.values = [[' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
        #                ['r', ' ', 'r', ' ', 'r', ' ', 'r', ' '],
        #                [' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
        #                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #                ['a', ' ', 'a', ' ', 'a', ' ', 'a', ' '],
        #                [' ', 'a', ' ', 'a', ' ', 'a', ' ', 'a'],
        #                ['a', ' ', 'a', ' ', 'a', ' ', 'a', ' ']]
        self.values = [[' ', 'r', ' ', 'r', ' '],
                       ['r', ' ', 'r', ' ', 'r'],
                       [' ', ' ', ' ', ' ', ' '],
                       ['a', ' ', 'a', ' ', 'a'],
                       [' ', 'a', ' ', 'a', ' ']]

        self.stack = []
        self.current_player = "a"

    def switch_player(self):
        self.current_player = 'a' if self.current_player == "r" else 'r'

    # def print(self):
    #     print()
    #     print("       0     1     2     3     4     5     6     7")
    #     print()
    #     print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
    #     for row in range(8):
    #         sys.stdout.write("{}   |".format(row))
    #         for col in range(8):
    #             sys.stdout.write("  {}  |".format(self.values[row][col]))
    #         print()
    #         print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
    #     print()
    #     # print("       0     1     2     3     4     5     6     7")

    def print(self):
        print()
        print("       0     1     2     3     4     5     6     7")
        print()
        print("    +-----+-----+-----+-----+-----+")
        for row in range(5):
            sys.stdout.write("{}   |".format(row))
            for col in range(5):
                sys.stdout.write("  {}  |".format(self.values[row][col]))
            print()
            print("    +-----+-----+-----+-----+-----+")
        print()
        # print("       0     1     2     3     4     5     6     7")

    def get_win(self):
        tab, order = self.get_possible_moves()
        if len(tab) == 0:
            return 'a' if self.current_player == 'r' else 'r'
        return None


    def make_move(self, move):
        # print("player " + self.whose_turn() + " turn")
        self.stack.append( [copy.deepcopy(self.values), self.whose_turn()] )
        # print("stack:")
        # print(self.stack)

        start_x = move[0][0]
        start_y = move[0][1]
        end_x = move[1][0]
        end_y = move[1][1]

        self.values[end_x][end_y] = self.values[start_x][start_y]

        if (end_x == 4 and self.values[end_x][end_y]=='r') or (end_x == 0 and self.values[end_x][end_y]=='a'):
            self.values[end_x][end_y] = self.values[end_x][end_y].upper()
        self.values[start_x][start_y] = ' '
        # print(abs(end_x - start_x))

        if abs(end_x - start_x) == 2:
            self.values[(end_x + start_x)//2][(end_y + start_y)//2] = ' '
            next_moves, order = self.get_possible_moves()
            if order == 1:
                self.switch_player()

        self.switch_player()


    def undo_move(self):
        self.values, self.current_player = self.stack.pop()
        pass


    def get_possible_moves(self):
        other_player = 'a' if self.current_player == 'r' else 'r'
        x1 = -1 if self.current_player == 'a' else 1
        y1 = -1
        x2 = -1 if self.current_player == 'a' else 1
        y2 =  1
        x3 =  1 if self.current_player == 'a' else -1
        y3 = -1
        x4 =  1 if self.current_player == 'a' else -1
        y4 = 1
        delta = [[-1, -1], [-1, 1], [1, -1], [1, 1]] if self.current_player == 'a' else [[1, -1], [1, 1], [-1, -1], [-1, 1]]

        list = []
        list_2 = []
        for row in range(len(self.values)):
            for kolm in range(len(self.values[row])):
                if self.values[row][kolm].lower() == self.current_player:

                    # the first option for a regular checker
                    new_row = row + x1
                    new_kolm = kolm + y1
                    if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]):
                        if self.values[new_row][new_kolm]== ' ':
                            list.append( [ [row, kolm] , [new_row, new_kolm] ] )
                        elif self.values[new_row][new_kolm].lower() == other_player:
                            new_row = new_row + x1
                            new_kolm = new_kolm + y1
                            if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]) and self.values[new_row][new_kolm]== ' ':
                                list_2.append([[row, kolm], [new_row, new_kolm]])

                    # the second option for a regular checker
                    new_row = row + x2
                    new_kolm = kolm + y2
                    if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]):
                        if self.values[new_row][new_kolm] == ' ':
                            list.append([[row, kolm], [new_row, new_kolm]])
                        elif self.values[new_row][new_kolm].lower() == other_player:
                            new_row = new_row + x2
                            new_kolm = new_kolm + y2
                            if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]) and self.values[new_row][new_kolm] == ' ':
                                list_2.append([[row, kolm], [new_row, new_kolm]])


                    if self.values[row][kolm].isupper():

                        # third option for King checker
                        new_row = row + x3
                        new_kolm = kolm + y3
                        if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]):
                            if self.values[new_row][new_kolm] == ' ':
                                list.append([[row, kolm], [new_row, new_kolm]])
                            elif self.values[new_row][new_kolm].lower() == other_player:
                                new_row = new_row + x3
                                new_kolm = new_kolm + y3
                                if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]) and \
                                        self.values[new_row][new_kolm] == ' ':
                                    list_2.append([[row, kolm], [new_row, new_kolm]])

                        # fourth option for King checker
                        new_row = row + x4
                        new_kolm = kolm + y4
                        if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(self.values[row]):
                            if self.values[new_row][new_kolm] == ' ':
                                list.append([[row, kolm], [new_row, new_kolm]])
                            elif self.values[new_row][new_kolm].lower() == other_player:
                                new_row = new_row + x4
                                new_kolm = new_kolm + y4
                                if 0 <= new_row < len(self.values) and 0 <= new_kolm < len(
                                        self.values[row]) and \
                                        self.values[new_row][new_kolm] == ' ':
                                    list_2.append([[row, kolm], [new_row, new_kolm]])
        if len(list_2) > 0:
            return list_2, 1
        else:
            return list, 2

    def whose_turn(self):
        return self.current_player
