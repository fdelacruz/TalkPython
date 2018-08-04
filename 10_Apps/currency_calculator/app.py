def main():
    print_header()

    amount = input('How much (USD) would you like to exchange?: ')
    
    print(amount)


def print_header():
    print('-----------------------')
    print('  Currency Calculator  ')
    print('-----------------------')
    print()


if __name__ == '__main__':
    main()
