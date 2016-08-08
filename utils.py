from getch import getch


def get_command():
    while True:
        try:
            command = getch()
        except OverflowError:
            print('change keyboard layout')
            continue
        if command in list('qwasd'):
            return command.lower()


def yes_no_prompt():
    print('(y/n)')
    command = ''
    while command not in ('y', 'n'):
        command = getch().lower()
    return command == 'y'
