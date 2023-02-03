import parsec as parsec


def __match_eol():
    windowsLineEndingParser = parsec.string('\r\n')
    unixLineEndingParser = parsec.string('\n')

    return parsec.choice( windowsLineEndingParser
                        , unixLineEndingParser
                        )

eol_parser = __match_eol()

eol_or_eof_parser = parsec.try_choice(eol_parser, parsec.eof())