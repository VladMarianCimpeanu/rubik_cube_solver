from colors import Color

class Face:
    def __init__(self, *args):
        self.face = []
        """if args length is 1, the argument must be a Color object and the face is initialized to a face with the selected color """
        """if args lenght is 2, the arguments must be 3 lists of 3 Colors. """
        if len(args) == 1:
            for row in range(3):
                self.face.append([])
                for column in range(3):
                    self.face[row].append(args[0].name)
        else:
            for item in args[0]:
                self.face.append(item)

    def get_row(self, row: int) -> list:
        return self.face[row].copy()

    def get_column(self, column: int) -> list:
        return [blocks[column] for blocks in self.face].copy()

    def set_row(self, row_index: int, blocks: list ) -> list:
        old_row = self.get_row(row_index)
        for index, color in enumerate(blocks):
            self.face[row_index][index] = color
        return old_row

    def set_column(self, column_index: int, blocks: list) -> list:
        old_column = self.get_column(column_index)
        index = 0
        for row in self.face:
            row[column_index] = blocks[index]
            index += 1
        return old_column

    def get_face(self):
        return Face([row.copy() for row in self.face], True)

    def print_face(self) -> None:
        for row in self.face:
            print(row)

    def is_monocolored(self) -> bool:
        face_color = self.face[0][0]
        for row in self.face:
            for column in row:
                if column != face_color:
                    return False
        return True

    def rotate_clockwise(self) -> None:
        temporary_face = self.get_face()
        for row in range(3):
            for column in range(3):
                (self.face)[row][column] = temporary_face.get_row(2 - column)[row]

    def rotate_counterclockwise(self) -> None:
        temporary_face = self.get_face()
        for row in range(3):
            for column in range(3):
                (self.face)[row][column] = temporary_face.get_row(column)[2 - row]

    def count_colors(self):
        result = []
        for color in Color:
            quantity = 0
            for row in self.face:
                quantity += row.count(color.name)
            result.append(quantity)
        return result

if __name__ == "__main__":
    face = Face(Color.RED)
    face.set_row(0, [Color.BLUE.name, Color.YELLOW.name, Color.WHITE.name])
    face.set_row(1, [Color.RED.name, Color.WHITE.name, Color.ORANGE.name])
    face.set_row(2, [Color.ORANGE.name, Color.GREEN.name, Color.RED.name])
    face.print_face()
    print("\n")
    face.set_column(2, [Color.BLUE.name, Color.WHITE.name, Color.GREEN.name])
    face.print_face()
    face.rotate_counterclockwise()
    print("\n")
    face.print_face()