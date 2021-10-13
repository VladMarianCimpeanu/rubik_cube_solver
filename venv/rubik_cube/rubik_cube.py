from colors import Color
from direction import Direction
from face import Face
from CubeExceptions import Faces_cube_Exception
import random

class Cube:
    """
    A cube is composed by 6 faces:
    Front face is 0
    Right face is 1
    Back face is 2
    Left face is 3
    Top face is 4
    Bottom face is 5

    If args is empty it will generate a solved cube.
    If args contain 5 faces it generates a cube with the given faces.
    """
    def __init__(self, *args):
        self.horizontal_direction = [1, 2, 3]
        self.vertical_direction = [4, 2, 5]
        self.faces = []
        if len(args) == 0:
            for color in (Color):
                self.faces.append(Face(color))
        elif len(args[0]) == 6:
            for face in args[0]:
                self.faces.append(face)
        else:
            raise Faces_cube_Exception(len(args[0]))

    def show_cube(self):
        for face in self.faces:
            face.print_face()
            print("----------------")

    def switch_columns(self, direction: list(), position: int) -> None:
        last_visited_face = 0
        last_visited_column = (self.faces[last_visited_face]).get_column(position)
        for face_to_visit in direction:
            last_visited_column = (self.faces[face_to_visit]).set_column(position, last_visited_column)
            last_visited_face = face_to_visit
        (self.faces[0]).set_column(position, last_visited_column)

    def switch_rows(self, direction: list(), position: int) -> None:
        last_visited_face = 0
        last_visited_row = (self.faces[last_visited_face]).get_row(position)
        for face_to_visit in direction:
            last_visited_row = (self.faces[face_to_visit]).set_row(position, last_visited_row)
            last_visited_face = face_to_visit
        (self.faces[0]).set_row(position, last_visited_row)

    def rotate(self, direction: Direction, position: int) -> None:
        if direction == direction.UP:
            self.switch_columns(self.vertical_direction, position)
            if position == 2:
                self.faces[1].rotate_clockwise()
            elif position == 0:
                self.faces[3].rotate_counterclockwise()
        elif direction == direction.DOWN:
            self.switch_columns(self.vertical_direction[::-1], position)
            if position == 2:
                self.faces[1].rotate_counterclockwise()
            elif position == 0:
                self.faces[3].rotate_clockwise()
        elif direction == direction.RIGHT:
            self.switch_rows(self.horizontal_direction, position)
            if position == 2:
                self.faces[5].rotate_clockwise()
            elif position == 0:
                self.faces[4].rotate_counterclockwise()
        else:
            self.switch_rows(self.horizontal_direction[::-1], position)
            if position == 2:
                self.faces[5].rotate_counterclockwise()
            elif position == 0:
                self.faces[4].rotate_clockwise()

    def get_face(self, face: int):
        return self.faces[face].get_face()

    def copy_cube(self) -> list:
        return [face.get_face() for face in self.faces]

    def is_solved(self) -> bool:
        for face in self.faces:
            if not face.is_monocolored():
                return False
        return True

    def shuffle(self, moves=200):
        directions = [dir for dir in Direction]
        for move in range(moves):
            direction = random.choice(directions)
            position = random.randint(0,2)
            self.rotate(direction, position)

    def is_feasible(self):
        quantities = [0, 0, 0, 0, 0, 0]
        for face in self.faces:
            face_quantity = face.count_colors()
            for index in range(6):
                quantities[index] += face_quantity[index]
        for item in quantities:
            if item != 9:
                return False
        return True



if __name__ == "__main__":
    cube = Cube()
    cube.show_cube()
    print("\n")
    cube.shuffle()
    cube.show_cube()
    print(cube.is_feasible())


