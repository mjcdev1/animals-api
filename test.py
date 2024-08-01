import os
import logging
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import AnimalsTable, AnimalClassesTable, AnimalOrdersTable, AnimalFamiliesTable
from models.models import AnimalSpeciesTable, AnimalSubspeciesTable
from models.models import MarkersTable, UsersTable

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv('database.env')

print(os.getenv('DATABASE_USER'))

# Database setup
DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Query the first animal
    animal = session.query(MarkersTable).first()
    if animal:
        logger.info(f"Queried animal: {animal.marker_title}")
    else:
        logger.info("No animals found in the database.")

except Exception as e:
    logger.exception("An error occurred: %s", e)
    session.rollback()
finally:
    session.close()
