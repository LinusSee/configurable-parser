import src.cli.cli_interface as ArgumentInterface
import src.cli_arguments_as_parsers as ArgumentMapping
import src.orchestration.orchestration as OC
import src.business_logic.parsing_config as ParsingConfig



def parse_with_arguments(cli_arguments):
    print(cli_arguments)
    # Apply interface and according validation
    parsed_arguments = ArgumentInterface.parse_arguments(cli_arguments)
    print("Parsed args: ", parsed_arguments)

    # Map to business model
    parsing_config = ArgumentMapping.config_from_parsed_cli_arguments(parsed_arguments)

    # Apply business logic (orchestration)
    return OC.parse_file(parsing_config)