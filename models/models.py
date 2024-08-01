from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Text, ARRAY, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AnimalsTable(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    common_name = Column(String(255), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey('classes.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    family_id = Column(Integer, ForeignKey('families.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    subspecies_id = Column(Integer, ForeignKey('subspecies.id'))
    scientific_name = Column(String(255), nullable=False, unique=True)
    conservation_status = Column(String(255), nullable=False)
    attributes = Column(JSON)
    header_img_url = Column(Text)
    addl_img_urls = Column(ARRAY(Text))
    species_desc = Column(Text)
    subspecies_desc = Column(Text)
    sources = Column(ARRAY(Text))
    
class AnimalClassesTable(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    
class AnimalOrdersTable(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey('classes.id'))
    
class AnimalFamiliesTable(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey('orders.id'))
    
class AnimalSpeciesTable(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey('families.id'))
    
class AnimalSubspeciesTable(Base):
    __tablename__ = 'subspecies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey('species.id'))
    
class MarkersTable(Base):
    __tablename__ = 'markers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mid = Column(String(50), nullable=False, unique=True)
    marker_lat_lon = Column(JSON, nullable=False)
    marker_location = Column(String(50), nullable=False)
    marker_title = Column(String(50), nullable=False)
    marker_date_placed = Column(TIMESTAMP, nullable=False)
    marker_placed_by_uid = Column(String(40), nullable=False)
    marker_status = Column(String(20), nullable=False)
    marker_animal_details = Column(JSON, nullable=False)
    marker_stats = Column(JSON, nullable=False)
    
class UsersTable(Base):
    __tablename__ = 'users'

    uid = Column(String(50), primary_key=True, nullable=False, unique=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    hashed_pw = Column(String(200), nullable=False)
    user_stats = Column(JSON)