import parsec as parsec

import src.business_logic.given_parser as GivenParser
import src.business_logic.until_end_parser as UntilEndParser
import src.business_logic.one_of_parser as OneOfParser
import src.business_logic.eol_parser as EolParser



def parse_file(filename, parser_configs):
    with open(filename) as file:
        file_content = file.read()
    print('----file contents start')
    print(file_content)
    print('----file contents end')

    return parse_text(file_content, parser_configs)



def parse_text(text, parser_configs):
    parsers = list(map(__parser_config_as_parser, parser_configs))
    joint_parsers_with_eol = parsec.joint(*parsers, EolParser.eol_or_eof_parser)

    final_parser = parsec.many(joint_parsers_with_eol)

    return parsec.parse(final_parser, text, 0)



def __parser_config_as_parser(parser_config):
    match parser_config.parser_type:
        case 'GivenParser':
            return GivenParser.match_string(parser_config.target_string, parser_config.header)
        case 'UntilEndParser':
            return UntilEndParser.match_end_of_line(parser_config.header)
        case 'OneOfParser':
            return OneOfParser.match_one_of(parser_config.target_values, parser_config.header)

    raise UnknownParserException(parser_config.parser_type)



class UnknownParserException(Exception):
    def __init__(self, unknown_parser_type):
        message = 'Can not create parser of type "{parser_type}", because the type is unknown'.format(parser_type=unknown_parser_type)
        super().__init__(message)