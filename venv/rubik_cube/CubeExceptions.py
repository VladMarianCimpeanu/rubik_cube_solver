class Faces_cube_Exception(Exception):
    def __init__(self, number_of_faces: int):
        self.message = "This cube has been initialized with {} faces but it should be have 6 faces.".format(number_of_faces)
        super().__init__(self.message)