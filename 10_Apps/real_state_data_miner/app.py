import os
import csv


def main():
    print_hearder()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_hearder():
    print('------------------------------------')
    print('       REAL ESTATE DATA MINER        ')
    print('------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print('Bed count {}:'.format(row['beds']))

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        # print(header.upper())
        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]
        #     print('Bed count {}:'.format(beds))


# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])


def query_data(data):
    pass


if __name__ == "__main__":
    main()
