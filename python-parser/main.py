import sys

import src.cli.api.cli_api as CliApi



multilineStringWindows = 'Loglevel: \r\nLoglevel: \r\nLoglevel: '


def main():
    parsing_result = CliApi.parse_with_arguments(sys.argv[1:])

    print(parsing_result)


if __name__ == '__main__':
    main()