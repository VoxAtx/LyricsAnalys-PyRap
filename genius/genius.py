import requests
from bs4 import BeautifulSoup as BS

import settings

token = 'Bearer ' + settings.access_token
base_url = "http://api.genius.com"
headers = {'Authorization': token}


def ge