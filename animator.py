from grid import Grid
import os


class Animator(object):
    cell_v_len = 3  # better to choose odd number
    cell_h_len = cell_v_len * 2 + 2

    def __init__(self, grid):
        self.grid = grid
        self.size = self.grid.size
        self.cells = self.empty_cells()

        """ grey shades. format: 48;2;<r>;<g>;<b>
            currently supported only by Xterm, KDE's Konsole
            self.colors = list(range(255, 0, -255 // (self.size ** 2) + 1))"""
        self.colors = list(range(41, 48))
        self.colors_num = len(self.colors)

    @staticmethod
    def map_cell_to_color(cell, code='40'):
        return '\033[1;30;{}m{}\033[0m'.format(code, cell)

    def empty_cells(self):
        return [[None] * self.size for _ in range(self.size * self.cell_v_len)]

    def fill_cells(self):
        for line in range(self.size * self.cell_v_len):
            y = line // self.cell_v_len
            center_of_cell = line % self.cell_v_len == self.cell_v_len // 2
            for x in range(self.size):
                tile = self.grid.content(x, y)
                if tile and center_of_cell:
                    self.cells[line][x] = str(tile.value).center(self.cell_h_len, ' ')
                else:
                    self.cells[line][x] = ' ' * self.cell_h_len

    def decorate_cells(self):
        for line in range(self.size * self.cell_v_len):
            y = line // self.cell_v_len
            for x in range(self.size):
                tile = self.grid.content(x, y)
                if tile:
                    index = self.colors[tile.value % self.colors_num]
                    self.cells[line][x] = self.map_cell_to_color(self.cells[line][x],
                                                                 str(index))
                else:
                    self.cells[line][x] = self.map_cell_to_color(self.cells[line][x])

    def show(self):
        self.fill_cells()
        self.decorate_cells()
        os.system('clear')
        for line in self.cells:
            print(''.join(map(str, line)))


def main():
    grid = Grid(4)
    anim = Animator(grid)
    anim.show()


if __name__ == '__main__':
    main()

