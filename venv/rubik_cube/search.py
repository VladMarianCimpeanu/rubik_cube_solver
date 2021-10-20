from node import Node
from rubik_cube import Cube

import numpy as np


class Iterative_deeping_search:
    def __init__(self, node: Node):
        self.root = node
        self.frontieer = np.array([self.root])

    def search(self):
        if self.root ==  None:
            return
        for deepness in range(21):
            found_node = self.iterative_deepening_search(deepness)
            if found_node is not None:
                return found_node
            self.frontieer = np.array([self.root])
        return None

    def iterative_deepening_search(self, maximum_depth: int):
        while self.frontieer.size != 0:
            node_to_expand = self.frontieer[-1]
            self.frontieer = self.frontieer[:-1]
            if node_to_expand.is_goal_node():
                return node_to_expand
            if node_to_expand.get_depth() < maximum_depth:
                self.frontieer = np.append(self.frontieer, node_to_expand.expand())
        return None

    def solve(self):
        last_node = self.search()
        if last_node is None:
            return np.array([])
        #in this array are stored all the nodes to reach the solution.
        moves_sequence = np.array([])
        while last_node is not None:
            moves_sequence = np.append([last_node], moves_sequence)
            last_node = last_node.get_parent()
        return moves_sequence

if __name__ == "__main__":
    cube = Cube()
    cube.shuffle()
    node = Node(cube, None, None, -1, 0)
    engine = Iterative_deeping_search(node)
    moves = engine.solve()
    print(len(moves))