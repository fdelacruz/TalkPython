import os


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
    pass

def query_data(data):
    pass


if __name__ == "__main__":
    main()
