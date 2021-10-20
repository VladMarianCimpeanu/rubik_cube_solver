from rubik_cube import Cube
from direction import Direction
import numpy as np

class Node:
    def __init__(self, cube, parent, used_direction, used_position, depth):
        self.cube = cube
        self.parent = parent
        self.obtained_from = used_direction
        self.positon_from = used_position
        self.depth = depth

    """return a list containing all nodes having a possible configuration can be obtained starting from this node.
    This function avoid generating a node containing the cube of this node's father."""
    def expand(self) -> list():
        possible_moves = np.array([])
        for dir in Direction:
            for pos in range(3):
                """it is avoiding to generate a child containing the same cube of its parent node."""
                if self.obtained_from is None or not (dir.is_opposite(self.obtained_from)
                        and pos == self.positon_from):
                    new_cube = self.cube.copy_cube()
                    new_cube.rotate(dir, pos)
                    possible_moves = np.append(possible_moves, [Node(new_cube, self, dir, pos, self.depth + 1)])
        return possible_moves

    """it returns a copy of its Cube."""
    def get_cube(self):
        return self.cube.copy_cube()

    """it returns True if the node is a terminal node(the cube is solved), otherwise False."""
    def is_goal_node(self):
        return self.cube.is_solved()

    def get_depth(self):
        return self.depth

    def get_parent(self):
        return self.parent


if __name__ == "__main__":
    node = Node(Cube(), None, None, -1, 0)
    print(node)
    print(node.is_goal_node())