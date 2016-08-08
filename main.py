from game_manager import GameManager
import argparse

DEFAULT_GRID_SIZE = 7
SHUFFLE_DELAY = 0.01  # set 0 for disable shuffle animation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="grid size",
                        type=int, default=DEFAULT_GRID_SIZE)
    parser.add_argument("-d", "--delay", help="shuffle delay",
                        type=float, default=SHUFFLE_DELAY)
    args = parser.parse_args()

    gm = GameManager(size=args.size, shuffle_delay=args.delay)
    gm.game_loop()


if __name__ == '__main__':
    main()
