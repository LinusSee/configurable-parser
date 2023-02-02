import parsec as parsec

def matchString(expectedString, header):
    parser = parsec.string(expectedString)
    parserMap = parsec.parsecmap(parser, lambda x : (header, x))

    return parserMap