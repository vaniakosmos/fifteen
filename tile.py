class Tile(object):
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def __str__(self):
        return '<Tile at ({}, {}) with {}>'.format(self.x, self.y, self.value)
