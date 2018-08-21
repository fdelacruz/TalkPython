import os
import csv

from data_types import Purchase


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
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

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
    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'
          .format(high_purchase.price, high_purchase.beds, high_purchase.baths))

    # lease expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'
          .format(low_purchase.price, low_purchase.beds, low_purchase.baths))
    # average price house?
    # average price of 2 bedroom houses
    pass


if __name__ == "__main__":
    main()
