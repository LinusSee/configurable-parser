import argparse


def __create_parser():
    parser = argparse.ArgumentParser(prog='Configurable Parser',
                            description='The parser can be configured via the commandline to process/parse files, to make them more readable')
    
    parser.add_argument('--input-file',
                        required=True,
                        help='The path to the file that should be parsed.')

    parser.add_argument('--output-file',
                        required=True,
                        help='The path of the file where the result should be written to.')

    parser.add_argument('--parser-string',
                        nargs=3,
                        action='append',
                        metavar=('<parser-position>', '<header-name>', '<target-string>'),
                        help='A string to match and the header value for the result.')
    
    parser.add_argument('--parser-until-end',
                        help='''Parses the rest of the line. The parameter requires the name of this parser.
                            \nThis parser can not be present more than once.
                            \nIt will always be the last parser to be executed.'''
                        )
    
    parser.add_argument('--parser-one-of',
                        nargs=3,
                        action='append',
                        metavar=('<parser-position>', '<header-name>', '<target-values>'),
                        help='''A comma separated list of values to match and the header value for the result.
                                Spaces after the comma will be treated as part of the oneOf string e.g.
                                    'INFO, INCIDENT,ERROR' becomes ['INFO', ' INCIDENT', 'ERROR']
                                For now this prevents commas to be part of a oneOf string.
                            ''')

    return parser



def parse_arguments(args):
    parser = __create_parser()

    parsed_args = parser.parse_args(args)

    if __has_at_least_one_parser_configured(parsed_args):
        return parsed_args

    parser.error('At least one parser has to be configured.')



def __has_at_least_one_parser_configured(parsed_args):
    if parsed_args.parser_string:
        return True

    return False