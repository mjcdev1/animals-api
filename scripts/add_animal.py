import requests
from dotenv import load_dotenv
import os

load_dotenv('database.env')


url = 'http://127.0.0.1:5000/add_animal_data'
url = (
    'https://animal-api-783131d61b3b.herokuapp.com/add_animal_data'
)  # -- IF TESTING WITH HEROKU
api_key = os.getenv('API_KEY')


data = {
    "common_name": "African bush sdff",
    "class_name": "Mammalia",
    "order_name": "Proboscidea",
    "family_name": "Elephantidae",
    "species_name": "Loxodonta africana",
    "subspecies_name": None,
    "scientific_name": "Loxodonta africanaaaasffafff",
    "conservation_status": "Endangered",
    "attributes": None,
    "header_img_url": None,
    "addl_img_urls": None,
    "species_desc": None,
    "subspecies_desc": None,
    "sources": None
}

response = requests.post(url, params={'api_key': api_key}, json=data)

if response.status_code == 200:
    print('Data added successfully:', response.json())
else:
    print('Failed to add data:', response.status_code, response.json())
