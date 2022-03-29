import requests
import json

def get_info(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    url = f'https://api.spoonacular.com'
    print(get_info(url))