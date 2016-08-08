from grid import Grid
from random import choice
import os
import sys
import select
from utils import *
from time import sleep
from animator import Animator


class GameManager(object):
    directions = {'up': (0, 1),
                  'right': (1, 0),
                  'down': (0, -1),
                  'left': (-1, 0)}

    opposites = {'up': 'down',
                 'down': 'up',
                 'left': 'right',
                 'right': 'left'}

    control = {'w': 'up',
               'a': 'right',
               's': 'down',
               'd': 'left'}

    def __init__(self, size, shuffle_delay):
        self.grid = Grid(size)
        self.last_dir = 'up'
        self.won = False
        self.shuffle_delay = shuffle_delay
        self.animator = Animator(self.grid)

    @staticmethod
    def get_vector(x, y, direction):
        bx, by = GameManager.directions[direction]  # bias x and y
        bx += x
        by += y
        return bx, by

    def move(self, x, y):
        if not self.grid.within_bounds(x, y):
            return 0

        chosen_tile = self.grid.content(x, y)
        if not chosen_tile:
            return '({}, {}) is empty tile'.format(x, y)

        for direction in GameManager.directions:
            bx, by = GameManager.get_vector(x, y, direction)
            if self.grid.within_bounds(bx, by) and not self.grid.content(bx, by):
                self.grid.move_tile(chosen_tile, bx, by)
                return 0
        return 'no empty tile near ({}, {})'.format(x, y)

    def random_move(self):
        ex, ey = self.grid.empty

        valid_dirs = []
        for direction in GameManager.directions:
            bx, by = GameManager.get_vector(ex, ey, direction)
            if self.grid.within_bounds(bx, by):
                valid_dirs.append(direction)

        if GameManager.opposites[self.last_dir] in valid_dirs:
            valid_dirs.remove(GameManager.opposites[self.last_dir])

        self.last_dir = choice(valid_dirs)
        x, y = GameManager.directions[self.last_dir]
        self.move(x + ex, y + ey)

    def shuffle_tiles(self, n, shuffle_sleep_time=None):
        print('Shuffling...')
        for _ in range(n):
            self.random_move()
            if shuffle_sleep_time:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.animator.show()
                print('Shuffling... Press Enter to stop')
                sleep(shuffle_sleep_time)
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    line = input()  # for avoiding double prompt and line removing
                    break

    def win_condition(self):
        return self.grid.perfect()

    def game_loop(self):
        self.shuffle_tiles(self.grid.size ** 2 * 80, self.shuffle_delay)
        os.system('clear')
        self.animator.show()
        print('WASD - control\t\tq - quit')

        while True:
            command = get_command()
            if command == 'q':
                print('Quit? ', end='')
                if yes_no_prompt():
                    print('\x1b[1A' + '\x1b[2K', end='')
                    print('\x1b[1A' + '\x1b[2K', end='')
                    print('''bye ( -_-)ノ\n''')
                    break

            message = None
            if command in 'wasd':
                x, y = self.grid.empty
                x, y = GameManager.get_vector(x, y, GameManager.control[command])
                message = self.move(x, y)

            os.system('clear')
            self.animator.show()
            print('WASD - control\t\tq - quit')
            if message:
                print(message)

            if command != 'q' and self.win_condition():
                print("YOU WIN")
                break


def foo(mat):
    print()
    for line in mat:
        print(' '.join(map(str, line)))


def main():
    gm = GameManager(5, 0.05)
    gm.game_loop()

if __name__ == '__main__':
    main()

