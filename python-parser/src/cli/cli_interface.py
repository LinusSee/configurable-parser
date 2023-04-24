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

    parser.add_argument('--parser-length',
                        nargs=3,
                        action=_ParserLengthAction,
                        metavar=('<parser-position>', '<header-name>', '<length>'),
                        help='A number of chars to match and the header value for the result.')

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



class _ParserLengthAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        print('\n\n\n', values)
        try:
            values[2] = int(values[2])

        except ValueError:
            message = 'Third argument "length" must be an integer, but {values} could not be converted'.format(values)
            raise argparse.ArgumentError(self, message)

        
        self.__append_values(namespace, values)


    def __append_values(self, namespace, values):
        existing_values = getattr(namespace, self.dest)

        if existing_values is None:
            existing_values = []

        existing_values.append(values)
        setattr(namespace, self.dest, existing_values)