import parsec as parsec

def match_string(expectedString, header):
    parser = parsec.string(expectedString)
    parserMap = parsec.parsecmap(parser, lambda parsedValue : (header, parsedValue))

    return parserMap