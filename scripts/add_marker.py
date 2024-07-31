"""TEMPORARY PLACEHOLDER DOCSTRING!"""

from datetime import datetime
import os

from dotenv import load_dotenv
import requests
from utilities import utils

load_dotenv('database.env')

url = 'http://127.0.0.1:5000/add_marker_data'
url = (
    'https://animal-api-783131d61b3b.herokuapp.com/add_marker_data'
)  # -- IF TESTING WITH HEROKU
api_key = os.getenv('API_KEY')

data = {
    "mid": utils.generate_id("marker"),
    "marker_lat_lon": '{"lat": "67.642676", "lon": "-18.407795"}',
    "marker_location": "Random Place, ON, CA",
    "marker_title": "I found a duck!",
    "marker_date_placed": datetime.now().isoformat(),
    "marker_placed_by_uid": "u_rgf234234_fake_uid",
    "marker_status": "active",
    "marker_animal_details": (
        '{"views": 0, "favorites": 0, '
        '"upvotes": 0, "downvotes": 0, "credibility_rating": 5.00}'
    ),
    "marker_stats": (
        '{"views": 0, "favorites": 0, '
        '"upvotes": 0, "downvotes": 0, "credibility_rating": 5.00}'
    )
}

response = requests.post(url, params={'api_key': api_key}, json=data)

if response.status_code == 200:
    print('Data added successfully:', response.json())
else:
    print('Failed to add data:', response.status_code, response.json())
