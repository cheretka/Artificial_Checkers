import sys

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Move:
    def __init__(self, p1, p2):
        self.start = p1
        self.end = p2


class Board:
    def __init__(self):
        self.values = [[' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
                       ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
                       [' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
                       [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
                       ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ']]
        self.stack = []
        self.current_player = "X"


    def print(self):
        print()
        print("       a     b     c     d     e     f     g     h")
        print()
        print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        for row in range(8):
            sys.stdout.write("{}   |".format(row+1))
            for col in range(8):
                sys.stdout.write("  {}  |".format(self.values[row][col]))
            print()
            print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        print()
        print("       a     b     c     d     e     f     g     h")


    def check_win(self):
        print(1)
        # countx =0
        # counto =0
        # for row in range(8):
        #     for col in range(8):
        #         if self.values[row][col] == 'X':
        #             countx +=1
        #         elif self.values[row][col] == 'O':
        #             counto +=1
        #
        # if countx==0:
        #     return 1
        # elif counto==0:
        #     return -1
        # else:
        #     return 0

    def get_possible_moves(self):
        delta1 = Position(-1, -1)  if self.current_player == 'X' else Position(1, -1)
        delta2 = Position(-1, 1) if self.current_player == 'X' else Position(1, 1)


        list = []
        for row in range(len(self.values)):
            for kolm in range(len(self.values[row])):
                if self.values[row][kolm] == self.current_player:
                    if 0 <= row + delta1.x < len(self.values) and 0 <= kolm + delta1.y < len(self.values[row]) and self.values[row + delta1.x][kolm + delta1.y]== ' ':
                        list.append( Move (Position(row, kolm), Position(row + delta1.x, kolm + delta1.y)) )
                    if 0 <= row + delta2.x < len(self.values) and 0 <= kolm + delta2.y < len(self.values[row]) and self.values[row + delta2.x][kolm + delta2.y]== ' ':
                        list.append( Move (Position(row, kolm), Position(row + delta2.x, kolm + delta2.y)) )

        return list
