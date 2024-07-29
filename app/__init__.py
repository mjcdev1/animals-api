from flask import Flask
from app.routes import init_routes
from database import Database
from database.db_ops import DBOps
import os
from dotenv import load_dotenv

load_dotenv('.env')

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    database = Database()
    db_ops = DBOps(database)
    
    init_routes(app, db_ops)
    
    return app
