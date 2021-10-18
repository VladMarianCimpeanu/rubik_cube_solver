import enum

class Direction(enum.Enum):
    UP = 1
    DOWN = -1
    RIGHT = 2
    LEFT = -2

    def is_opposite(self, direction):
        return self.value == -direction.value

if __name__ == "__main__":
    """should be TRUE"""
    print(Direction.UP.is_opposite(Direction.DOWN))
    """should be FALSE"""
    print(Direction.UP.is_opposite(Direction.RIGHT))
