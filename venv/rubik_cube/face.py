from colors import Color

class Face:
    def __init__(self, color: Color):
        self.face = []
        for row in range(3):
            self.face.append([])
            for column in range(3):
                self.face[row].append(color.name)

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

    def print_face(self) -> None:
        for row in self.face:
            print(row)

if __name__ == "__main__":
    face = Face(Color.RED)
    face.print_face()
    temp_row = face.get_row(0)
    face.set_row(0, [Color.BLUE.name for item in range(3)])
    print(temp_row)
    print("\n")
    face.print_face()
