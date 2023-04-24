import csv



def read_csv_as_parsing_data(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        content = list(reader)

    headers = content[0]
    parsing_data = map(lambda values: tuple(zip(headers, values)), content[1:])

    return list(parsing_data)
        