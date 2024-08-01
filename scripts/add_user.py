"""TEMPORARY PLACEHOLDER DOCSTRING!"""

import os

from dotenv import load_dotenv
import requests
from utilities import utils

load_dotenv('database.env')

url = 'http://127.0.0.1:5000/add_user_data'
url = (
    'https://animal-api-783131d61b3b.herokuapp.com/add_user_data'
)  # -- IF TESTING WITH HEROKU
api_key = os.getenv('API_KEY')

data = {
    "uid": utils.generate_id("user"),
    "username": 'temp',
    "email": "temp@temp",
    "hashed_pw": "f93fef_fake_hashed_pw_2f234324",
    "user_stats": (
        '{"upvotes": 0, "downvotes": 0, '
        '"points": 0, "favorites": 0, "credibility_rating": 5.00}'
    )
}

response = requests.post(url, params={'api_key': api_key}, json=data)

if response.status_code == 200:
    print('Data added successfully:', response.json())
else:
    print('Failed to add data:', response.status_code, response.json())
