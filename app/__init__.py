"""TEMPORARY PLACEHOLDER DOCSTRING!"""

from app.routes import init_routes
from database import Database
from database.db_ops import DBOps
from dotenv import load_dotenv
from flask import Flask

load_dotenv('.env')


def create_app() -> Flask:
    """TEMPORARY PLACEHOLDER DOCSTRING!"""
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    database = Database()
    db_ops = DBOps(database)

    init_routes(app, db_ops)

    return app
