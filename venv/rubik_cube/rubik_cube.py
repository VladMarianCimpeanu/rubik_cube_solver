from colors import Color
from direction import Direction
from face import Face

class Cube:

    def __init__(self, *args):
        self.horizontal_direction = [1, 3, 2, 0]
        self.vertical_direction = [4, 3, 5, 0]
        self.faces = []
        if len(args) == 0:
            for color in (Color):
                self.faces.append(Face(color))
        else:
            for face in args[0]:
                self.faces.append(face)

    def show_cube(self):
        for face in self.faces:
            face.print_face()

    def switch_columns(self, direction: list(), position: int) -> None:
        last_visited_face = 0
        last_visited_column = (self.faces[last_visited_face]).get_column(position)
        for face_to_visit in direction:
            last_visited_column = (self.faces[face_to_visit]).set_column(position, last_visited_column)
            last_visited_face = face_to_visit

    def switch_rows(self, direction: list(), position: int) -> None:
        last_visited_face = 0
        last_visited_row = (self.faces[last_visited_face]).get_row(position)
        for face_to_visit in direction:
            last_visited_row = (self.faces[face_to_visit]).set_row(position, last_visited_row)
            last_visited_face = face_to_visit

    def rotate(self, direction: Direction, position: int) -> None:
        if direction == direction.UP:
            self.switch_columns(self.vertical_direction, position)
        elif direction == direction.DOWN:
            self.switch_columns(self.vertical_direction.reverse(), position)
        elif direction == direction.RIGHT:
            self.switch_rows(self.horizontal_direction, position)
        else:
            self.switch_rows(self.horizontal_direction.reverse(), position)

    def get_face(self, face: int):
        return self.faces[face].get_face()

    def get_cube(self) -> list:
        return [face.get_face() for face in self.faces]


if __name__ == "__main__":
    cube = Cube()
    other_cube = Cube(cube.get_cube())
    other_cube.rotate(Direction.UP, 2)
    cube.show_cube()
    print("\n\n")
    other_cube.show_cube()


