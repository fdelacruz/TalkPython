import requests

def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)

def get_data_from_url(url):
    response = requests.get(url)
    return response.raw
