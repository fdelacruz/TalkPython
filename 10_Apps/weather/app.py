import requests
import bs4


def main():
    print_header()

    code = input('What zipcode do you want the weather for (972101)? ')

    html = get_html_from_web(code)

    report = get_weather_from_html(html)
    print(f'The temp in {report[3]} is {report[1]} {report[2]}')


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


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_loc(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return condition, temp, scale, loc  #tuple return


def find_city_and_state_from_loc(loc):
    parts = loc.split('\n')
    return parts[0].strip()

def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
