import keyboard
from collections import deque
from Paths_to_artifacts import PathsToArtifacts


def nl_command(args):
    if args.nl:
        path_to_dir = PathsToArtifacts.PATH_TO_ARTIFACTS.value
        file = path_to_dir + args.nl
    else:
        file = None

    if file:
        with open(file, 'r', encoding="utf-8") as f:
            count = 1
            while True:
                line = f.readline()
                if line:
                    print(f'{count}  {line}', end='')
                    count += 1
                else:
                    break
    else:
        count = 1
        try:
            while not keyboard.is_pressed('ctrl+d'):
                try:
                    print(f'{count}  {input()}')
                    count += 1
                except EOFError:
                    pass
            print('Ctrl+D was pressed')
        except KeyboardInterrupt:
            pass


def tail_command(args):
    files = ''
    if args.tail:
        path_to_dir = PathsToArtifacts.PATH_TO_ARTIFACTS.value
        files = [path_to_dir + file for file in args.tail]
    if not files:
        last_lines = deque(maxlen=17)
        try:
            while not keyboard.is_pressed('ctrl+d'):
                try:
                    last_lines.append(input().strip())
                except EOFError:
                    break
            print('Ctrl+D was pressed')
        except KeyboardInterrupt:
            pass
        for line in last_lines:
            print(line)
    else:
        for file in files:
            with open(file, 'r', encoding="utf-8") as f:
                if len(files) > 1:
                    print(f'==> {file} <==')
                for line in deque(f, 10):
                    print(line.strip())
                print('\n')


def wc_command(args):
    files = ''
    if args.wc:
        path_to_dir = PathsToArtifacts.PATH_TO_ARTIFACTS.value
        files = [path_to_dir + file for file in args.wc]
    if not files:
        count_lines = 0
        count_words = 0
        count_bytes = 0
        count_switches = 0
        try:
            while not keyboard.is_pressed('ctrl+d'):
                try:
                    count_switches += 1  # number of enter
                    users_input = input()
                    count_words += len(users_input.split())
                    count_lines += 1
                    count_bytes += len(users_input.encode('utf-8'))

                except EOFError:
                    break
            print('Ctrl+D was pressed')
        except KeyboardInterrupt:
            pass
        print(
            f'{count_lines} {count_words} {count_bytes + count_switches - 1}')  # adding the number
        # of newline transitions to the number of bytes
    else:
        count_lines_total = 0
        count_words_total = 0
        count_bytes_total = 0
        for file in files:
            with open(file, 'r', encoding="utf-8") as f:
                count_lines = sum(1 for line in f)
                count_lines_total += count_lines
                f.seek(0)
                count_words = sum(len(line.split()) for line in f)
                count_words_total += count_words
                f.seek(0, 2)
                count_bytes = f.tell()
                count_bytes_total += count_bytes  # in windows, the transition to a new line is performed via \r\n
                print(f'{count_lines} {count_words} {count_bytes} {file}')
        if len(files) > 1:
            print(f'{count_lines_total} {count_words_total} {count_bytes_total} total')
