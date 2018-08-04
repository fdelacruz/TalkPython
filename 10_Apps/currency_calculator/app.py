import requests


def main():
    print_header()

    amount = input('How much (USD) would you like to exchange?: ')

    html = get_html_from_web(amount)


def print_header():
    print('-----------------------')
    print('  Currency Calculator  ')
    print('-----------------------')
    print()


def get_html_from_web(amount):
    url = f'https://x-rates.com/calculator/?from=USD&to=INR&amount={amount}'
    response = requests.get(url)

    return response.text


if __name__ == '__main__':
    main()
