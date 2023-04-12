import src.business_logic.parsing_config as ParsingConfig

import src.business_logic.given_parser as GivenParser
import src.business_logic.until_end_parser as UntilEndParser



def config_from_parsed_cli_arguments(parsed_arguments):
    input_filename = parsed_arguments.input_file
    output_filename = parsed_arguments.output_file
    
    parser_configs = __map_cli_arguments_to_parsers(parsed_arguments.parser_string)

    if(parsed_arguments.parser_until_end is not None):
        parser_configs.append(UntilEndParser.UntilEndParser(parsed_arguments.parser_until_end))

    return ParsingConfig.ParsingConfig(input_filename, output_filename, parser_configs)



def __map_cli_arguments_to_parsers(cli_arguments):
    # Sort by position
    cli_arguments.sort(key=lambda argument: argument[0])
    print("Arguments after sort: ", cli_arguments)
    return list(map(__map_cli_argument_to_parser, cli_arguments))



def __map_cli_argument_to_parser(cli_argument):
    print("---------FINDME: ", cli_argument)
    given_parser = GivenParser.GivenParser(cli_argument[1], cli_argument[2])

    return given_parser