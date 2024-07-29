import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('database.env')

url = 'http://127.0.0.1:5000/get_animals'
url = 'https://animal-api-783131d61b3b.herokuapp.com/get_animals' #-- IF TESTING WITH HEROKU 
api_key = os.getenv('API_KEY')  

requested_items = {
    "common_name": "African bush sdff",
}

response = requests.get(url, params={'api_key': api_key}, json=requested_items)

if response.status_code == 200:
        print(response.json())
else:
        print(response.status_code, response.json())