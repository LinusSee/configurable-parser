import parsec as parsec
import functools



def match_one_of(expected_values, header):
    parsers = [parsec.string(expected_value) for expected_value in expected_values]
    parser = functools.reduce(parsec.try_choice, parsers)
    parserMap = parsec.parsecmap(parser, lambda parsed_value: (header, parsed_value))

    return parserMap



class OneOfParser:
    def __init__(self, header, target_values):
        self.parser_type = 'OneOfParser'
        self.header = header
        self.target_values = target_values

    def __str__(self):
        return 'A OneOfParser with the header "{self.header}" matching one of the following values: {self.target_values}'.format(self=self)