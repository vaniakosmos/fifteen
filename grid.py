from tile import Tile


class Grid(object):
    def __init__(self, size):
        self.size = size
        self._cells = self.empty_cells()
        self.setup_tiles()
        self.empty = (self.size - 1, self.size - 1)

        self._perfect_state = self.make_cells_copy()

    def make_cells_copy(self):
        clone = self.empty_cells()
        for y in range(self.size):
            for x in range(self.size):
                clone[y][x] = self._cells[y][x]
        return clone

    def perfect(self):
        for y in range(self.size):
            for x in range(self.size):
                a = self._perfect_state[y][x]
                b = self._cells[y][x]
                if (a and b and a.value != b.value) or (not a and b or a and not b):
                    return False
        return True

    def empty_cells(self):
        return [[None] * self.size for _ in range(self.size)]

    def setup_tiles(self):
        for y in range(self.size):
            for x in range(self.size):
                if (x + 1) * (y + 1) != self.size ** 2:
                    self._cells[y][x] = Tile(self.size * y + x + 1, x=x, y=y)

    def move_tile(self, tile, x, y):
        self._cells[y][x] = Tile(tile.value, x, y)
        self._cells[tile.y][tile.x] = None
        self.empty = (tile.x, tile.y)

    def content(self, x, y):
        return self._cells[y][x]

    def __str__(self):
        out = ''
        cell_length = 5
        for y in range(self.size):
            for x in range(self.size):
                tile = self._cells[y][x]
                if tile:
                    out += str(tile.value).center(cell_length, ' ') + '|'
                else:
                    out += ' ' * cell_length + '|'
            out += '\n' + '-' * (cell_length + 1) * self.size + '\n'
        return out

    def within_bounds(self, x, y):
        return (0 <= x < self.size and
                0 <= y < self.size)


def main():
    grid = Grid(4)
    print(grid)


if __name__ == '__main__':
    main()

