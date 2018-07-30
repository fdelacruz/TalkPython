def main():
    print_header()

    code = input('What zipcode do you want the weather for (972101)? ')

    print(code)


def print_header():
    print('-------------------------')
    print('         WEATHER         ')
    print('-------------------------')
    print()


def get_html_from_web(zipcode):
    url = f'wunderground.com/weather-forecast/{zipcode}'
    print(url)


if __name__ == '__main__':
    main()
