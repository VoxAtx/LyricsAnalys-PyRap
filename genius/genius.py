import requests
from bs4 import BeautifulSoup as BS

import settings

token = 'Bearer ' + settings.access_token
base_url = "http://api.genius.com"
headers = {'Authorization': token}


def get_url(url):
    '''
    Get Lyrics for a song given the Genius Web URL
    '''
    page = requests.get(url)
    html = BS(page.text, "html.parser")
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class