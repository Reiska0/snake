class ObjectCoordinates:
    def __init__(self, x = 0, y = 0):
        self.x = x if x != 0 else 5
        self.y = y if y != 0 else 4
    def copy(self):
        return ObjectCoordinates(self.x, self.y)
