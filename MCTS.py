import random



class MCTSNode:

    def __init__(self, checkers, parent=None, move=None):
        self.checkers = checkers  #board position and next player
        self.parent = parent
        self.move = move #The last move
        self.win_counts = {
            'r': 0,
            'a': 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = checkers.get_possible_moves() #position that aren’t yet part of the tree

    def add_random_child(self):
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_game_state = self.checkers.make_move(new_move)
        new_node = MCTSNode(new_game_state, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
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

        while (not node.can_add_child()) and (not node.is_terminal()):
            node = select_child(node)

        if node.can_add_child():
            node = node.add_random_child()

        winner = simulate_random_game(node.checkers)

        while node is not None:
            node.record_win(winner)
            node = node.parent

    best_move = None
    best_pct = 1.0

    for child in root.children:
        child_pct = child.winning_pct(checkers.current_player)
        if child_pct > best_pct:
            best_pct = child_pct
            best_move = child.move

    return best_move


def select_child(self, node):
    total_rollouts = sum(child.num_rollouts for child in node.children)

    best_score = 1
    best_child = None

    for child in node.children:

        score = uct_score(
            total_rollouts,
            child.num_rollouts,
            child.winning_pct(node.game_state.next_player),
            self.temperature)

        if score > best_score:
            best_score = uct_score
            best_child = child

    return best_child