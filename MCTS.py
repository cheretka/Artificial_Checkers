import random
from math import inf
import math

class MCTSNode:

    def __init__(self, checkers, parent=None, move=None):
        self.checkers = checkers  # board position and next player
        self.parent = parent
        self.move = move  # The last move
        self.win_counts = {
            'r': 0,
            'a': 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = self.checkers.get_possible_moves()  # position that aren’t yet part of the tree

    def __str__(self):
        return "\nmove: " + str(self.move) + "\nnum_rollouts: " + str(self.num_rollouts) \
               + "\nwin r: " + str(self.win_counts["r"]) + " win a: " + str(
            self.win_counts["a"]) + "\nchildren: " + str(self.children) + "\nunvisited_moves: " + str(
            self.unvisited_moves)

    def add_random_child(self):
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_checkers = self.checkers.make_move(new_move)
        new_node = MCTSNode(new_checkers, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        if winner == 'r' or winner == 'a':
            self.win_counts[winner] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        return self.checkers.get_win() is None

    def winning_pct(self, player):
        return float(self.win_counts[player]) / float(self.num_rollouts)


def uct_score(parent_rollouts, child_rollouts, win_pct, temperature):
    exploration = math.sqrt(math.log(parent_rollouts) / child_rollouts)
    return win_pct + temperature * exploration


def select_move(checkers, num_rounds):
    root = MCTSNode(checkers)

    for i in range(num_rounds):

        node = root

        while (not node.can_add_child()) and (node.is_terminal()) and len(node.children)>0:
            node = select_child(node)

        if node.can_add_child():
            node = node.add_random_child()

        winner = simulate_random_game(node.checkers)

        while node is not None:
            node.record_win(winner)
            node = node.parent

    best_move = None
    best_pct = -inf

    for child in root.children:
        child_pct = child.winning_pct(checkers.current_player)
        print("move: " + str(child.move) + "  ptc: " + str(round(child_pct, 3)))
        if child_pct > best_pct:
            best_pct = child_pct
            best_move = child.move

    print("selected move: " + str(best_move))
    return best_move


def select_child(node):
    total_rollouts = sum(child.num_rollouts for child in node.children)

    best_score = -inf
    best_child = None

    for child in node.children:

        exploration = math.sqrt(math.log(total_rollouts) / child.num_rollouts)
        score = child.winning_pct(node.checkers.current_player) + 0.7 * exploration

        if score > best_score:
            best_score = score
            best_child = child

    return best_child


def simulate_random_game(checkers):
    while checkers.get_win() is None:
        move = random.choice(checkers.get_possible_moves())
        checkers = checkers.make_move(move)

    return checkers.get_win()
