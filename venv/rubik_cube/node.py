from rubik_cube import Cube
from direction import Direction

class Node:
    def __init__(self, cube, parent, used_direction, used_position, depth):
        self.cube = cube
        self.parent = parent
        self.obtained_from = used_direction
        self.positon_from = used_position
        self.depth = depth

    def expand(self) -> list():
        possible_moves = []
        for dir in Direction:
            for pos in range(3):
                """it is avoiding to generate a child containing the same cube of its parent node."""
                if not ((self.obtained_from is None or dir.value == -self.obtained_from.value)
                        and pos == self.positon_from):
                    new_cube = self.cube.copy_cube()
                    new_cube.rotate(dir, pos)
                    possible_moves.append(Node(new_cube, self, dir, pos, self.depth + 1))
        return possible_moves

    def get_cube(self):
        return self.cube.copy_cube()




if __name__ == "__main__":
    node = Node(Cube(), None, None, -1, 0)
    new_nodes = node.expand()
    for item in new_nodes:
        item.get_cube().show_cube()