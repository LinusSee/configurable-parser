import sys

import src.cli.cli_arguments as cli_arguments
from src.orchestration import parse_file
import src.given_parser as GivenParser
import src.cli_arguments_as_parsers as ArgumentMapping



multilineStringWindows = 'Loglevel: \r\nLoglevel: \r\nLoglevel: '


def main():
    args = cli_arguments.parse_arguments(sys.argv[1:])

    parsers = ArgumentMapping.map_cli_arguments_to_parsers([args.parser_string])
    print(parse_file(args.input_file, parsers))


if __name__ == '__main__':
    main()