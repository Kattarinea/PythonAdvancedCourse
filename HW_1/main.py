import argparse
from commands import nl_command, tail_command, wc_command


def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-nl', nargs='?', const='', help='Выполнение команды nl')
    group.add_argument('-tail', nargs='*', default=None, help='Выполнение команды tail')
    group.add_argument('-wc', nargs='*', default=None, help='Выполнение команды wc')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.nl is not None:
        nl_command(args=args)
    elif args.tail is not None:
        tail_command(args=args)
    elif args.wc is not None:
        wc_command(args=args)
    else:
        raise Exception
