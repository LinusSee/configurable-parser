import parsec as parsec


def __matchEol():
    windowsLineEndingParser = parsec.string('\r\n')
    unixLineEndingParser = parsec.string('\n')

    return parsec.choice( windowsLineEndingParser
                        , unixLineEndingParser
                        )

eolParser = __matchEol()

eolOrEofParser = parsec.try_choice(eolParser, parsec.eof())