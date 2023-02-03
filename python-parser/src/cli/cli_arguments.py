import argparse


def __create_parser():
    parser = argparse.ArgumentParser(prog='Configurable Parser',
                            description='The parser can be configured via the commandline to process/parse files, to make them more readable')

    parser.add_argument('--input-file',
                        required=True,
                        help='The path to the file that should be parsed.')

    return parser


def parse_arguments():
    parser = __create_parser()

    return parser.parse_args()