import parsec as parsec

import src.business_logic.char_parser as CharParser
import src.business_logic.eol_parser as EolParser


def match_end_of_line(header):
    parser_until_end = parsec.many(CharParser.char_parser).ends_with(EolParser.eol_or_eof_parser)
    parser = parsec.parsecmap(parser_until_end, lambda values: ''.join(values))

    parserMap = parsec.parsecmap(parser, lambda parsedValue: (header, parsedValue))

    return parserMap



class UntilEndParser:
    def __init__(self, header):
        self.parser_type = 'UntilEndParser'
        self.header = header

    def __str__(self):
        return 'An UntilEndParser with the header "{self.header}"'.format(self=self)