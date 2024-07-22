from flask import Flask
import json
import psycopg2
from typing import Any, Dict
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

data = {
    "database_name": os.getenv('DATABASE_NAME'),
    "database_host": os.getenv('DATABASE_HOST'),
    "database_user": os.getenv('DATABASE_USER'),
    "database_pw": os.getenv('DATABASE_PW'),
    "database_port": os.getenv('DATABASE_PORT')
}

print(data)
print(data["database_name"])

def connect_to_database():
    conn = psycopg2.connect(
        dbname=data["database_name"],
        user=data["database_user"],
        password=data["database_pw"],
        host=data["database_host"],
        port=data["database_port"]
    )
    return conn

@app.route('/')
def index():
    conn = connect_to_database()
    conn.close()
    return 'Connected!'

@app.route('/animal', methods=['GET'])
def get_animal():
    return "This is a placeholder response for the /animal endpoint."

if __name__ == '__main__':
    app.run(debug=True)
