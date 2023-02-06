import csv


def remove_eol_eof_column(actual: list[(any)]):
    ''' Remove the last field of each row containing eol/eof.
        The field doesn't add any value to the tests and only causes them to
        break if its structure were to change.
    '''
    removal_fn = lambda row: row[:-1]

    return list(map(removal_fn, actual))



def read_csv_as_parsing_data(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        content = list(reader)

    headers = content[0]
    parsing_data = map(lambda values: tuple(zip(headers, values)), content[1:])

    return list(parsing_data)
        