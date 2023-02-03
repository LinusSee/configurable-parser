import argparse

import src.cli.cli_arguments as cli_arguments
from src.orchestration import parse_file



multilineStringWindows = 'Loglevel: \r\nLoglevel: \r\nLoglevel: '


def main():
    args = cli_arguments.parse_arguments()
    print('Arguments:')
    print(args)

    print(parse_file(args.input_file))


if __name__ == '__main__':
    main()