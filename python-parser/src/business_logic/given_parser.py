import parsec as parsec



def match_string(expectedString, header):
    parser = parsec.string(expectedString)
    parserMap = parsec.parsecmap(parser, lambda parsed_value: (header, parsed_value))

    return parserMap



class GivenParser:
    def __init__(self, header, target_string):
        self.parser_type = 'GivenParser'
        self.header = header
        self.target_string = target_string

    def __str__(self):
        return 'A given parser with the header "{self.header}" and the target string "{self.target_string}"'.format(self=self)

