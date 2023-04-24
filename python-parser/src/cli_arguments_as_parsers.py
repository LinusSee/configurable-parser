import src.business_logic.parsing_config as ParsingConfig

import src.business_logic.given_parser as GivenParser
import src.business_logic.match_for_parser as MatchForParser
import src.business_logic.until_end_parser as UntilEndParser
import src.business_logic.one_of_parser as OneOfParser



def config_from_parsed_cli_arguments(parsed_arguments):
    input_filename = parsed_arguments.input_file
    output_filename = parsed_arguments.output_file
    
    string_configs = __get_parser_string_configs(parsed_arguments.parser_string)
    length_configs = __get_parser_length_configs(parsed_arguments.parser_length)
    one_of_configs = __get_parser_one_of_configs(parsed_arguments.parser_one_of)
    parser_configs = __sorted_parser_configs([*string_configs, *length_configs, *one_of_configs])

    if(parsed_arguments.parser_until_end is not None):
        parser_configs.append(UntilEndParser.UntilEndParser(parsed_arguments.parser_until_end))

    return ParsingConfig.ParsingConfig(input_filename, output_filename, parser_configs)



def __sorted_parser_configs(parser_configs):
    print('CONFIGS ARE: ', parser_configs)
    parser_configs.sort(key=lambda argument: argument[0])

    return list(map(lambda config: config[1], parser_configs))


def __get_parser_string_configs(parser_string_arguments):
    if parser_string_arguments is None:
        return []

    map_parser_string = lambda arg: (arg[0], GivenParser.GivenParser(arg[1], arg[2]))

    return list(map(map_parser_string, parser_string_arguments))


def __get_parser_length_configs(parser_string_arguments):
    if parser_string_arguments is None:
        return []

    map_parser_string = lambda arg: (arg[0], MatchForParser.MatchForParser(arg[1], arg[2]))

    return list(map(map_parser_string, parser_string_arguments))



def __get_parser_one_of_configs(parser_one_of_arguments):
    if parser_one_of_arguments is None:
        return []

    map_parser_one_of = lambda arg: (arg[0], OneOfParser.OneOfParser(arg[1], arg[2].split(',')))
    return list(map(map_parser_one_of, parser_one_of_arguments))