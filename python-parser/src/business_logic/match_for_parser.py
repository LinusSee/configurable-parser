import parsec as Parsec

import src.business_logic.char_parser as CharParser


def match_for(count, header):
    parser_count = Parsec.count(CharParser.char_parser, count)
    parser = Parsec.parsecmap(parser_count, lambda values: ''.join(values))

    parserMap = Parsec.parsecmap(parser, lambda parsed_value: (header, parsed_value))

    return parserMap



class MatchForParser:
    def __init__(self, header, count):
        self.parser_type = 'MatchForParser'
        self.header = header
        self.count = count

    
    def __str__(self):
        return 'A MatchForParser with the header "{self.header}" matching exactely "{self.count}" chars'.format(self=self)
