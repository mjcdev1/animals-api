"""TEMPORARY PLACEHOLDER DOCSTRING!"""

import os

from dotenv import load_dotenv
import requests

load_dotenv('database.env')

url = 'http://127.0.0.1:5000/get_marker'
url = (
    'https://animal-api-783131d61b3b.herokuapp.com/get_marker'
)  # -- IF TESTING WITH HEROKU
api_key = os.getenv('API_KEY')

req_marker = "m_e2ca3749-df3e-4c57-a4c3-cd7be89ad116"

response = requests.get(url, params={'api_key': api_key, 'req_marker': req_marker})

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.json())
