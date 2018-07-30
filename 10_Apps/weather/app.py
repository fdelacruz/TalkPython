import requests


def main():
    print_header()

    code = input('What zipcode do you want the weather for (972101)? ')

    html = get_html_from_web(code)


def print_header():
    print('-------------------------')
    print('         WEATHER         ')
    print('-------------------------')
    print()


def get_html_from_web(zipcode):
    url = f'http://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


if __name__ == '__main__':
    main()
