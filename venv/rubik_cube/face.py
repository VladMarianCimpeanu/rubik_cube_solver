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
        for row in self.face:
            row[column_index] = blocks[column_index]
        return old_column

    def get_face(self):
        return Face([row.copy() for row in self.face], True)

    def print_face(self) -> None:
        for row in self.face:
            print(row)

if __name__ == "__main__":
    face = Face(Color.RED)
    copied_face = face.get_face()
    copied_face.set_row(0, [Color.BLUE.name for item in range(3)])
    face.print_face()
    copied_face.print_face()
