import src.business_logic.parsing_config as ParsingConfig

import src.business_logic.given_parser as GivenParser



def config_from_parsed_cli_arguments(parsed_arguments):
    input_filename = parsed_arguments.input_file
    output_filename = parsed_arguments.output_file
    parser_configs = __map_cli_arguments_to_parsers([parsed_arguments.parser_string])

    return ParsingConfig.ParsingConfig(input_filename, output_filename, parser_configs)



def __map_cli_arguments_to_parsers(cli_arguments):
    return list(map(__map_cli_argument_to_parser, cli_arguments))



def __map_cli_argument_to_parser(cli_argument):
    given_parser = GivenParser.GivenParser(cli_argument[0], cli_argument[1])

    return given_parser