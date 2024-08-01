"""TEMPORARY PLACEHOLDER DOCSTRING!"""

from typing import Any, Dict, List

from database import Database
import psycopg2
from queries import db_queries


class DBOps:
    """TEMPORARY PLACEHOLDER DOCSTRING!"""

    def __init__(self, database: Database) -> None:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        self.database = database

    def add_animal_data(self, data: Dict[str, Any]) -> Dict[str, str]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None

        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()

            conn.autocommit = False

            query = db_queries.ADD_CLASS
            cursor.execute(query, (data['class_name'],))

            query = db_queries.ADD_ORDER
            cursor.execute(query, (data['order_name'], data['class_name']))

            query = db_queries.ADD_FAMILY
            cursor.execute(query, (data['family_name'], data['order_name']))

            query = db_queries.ADD_SPECIES
            cursor.execute(query, (data['species_name'], data['family_name']))

            if data['subspecies_name']:
                query = db_queries.ADD_SUBSPECIES
                cursor.execute(
                    query,
                    (data['subspecies_name'], data['species_name'])
                )

            query = db_queries.ADD_ANIMAL
            cursor.execute(query, (
                data['common_name'],
                data['class_name'],
                data['order_name'],
                data['family_name'],
                data['species_name'],
                data['subspecies_name'],
                data['scientific_name'],
                data['conservation_status'],
                data.get('attributes', None),
                data.get('header_img_url', None),
                data.get('addl_img_urls', None),
                data.get('species_desc', None),
                data.get('subspecies_desc', None),
                data.get('sources', None)
            ))

            conn.commit()

            return {"message": "Data added successfully."}

        except psycopg2.Error as e:
            if conn:
                conn.rollback()
            if 'unique_violation' in str(e):
                return {
                    "error": "Unique constraint violation: Duplicate record exists."
                }
            return {"error": f"SQL Error: {str(e)}"}

        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)

    def get_animals_data(self, requested_data: Dict[str, str]) -> List[Dict[str, Any]]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None

        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()

            query = db_queries.GET_ANIMALS

            filter_condition = ""
            param = None

            if requested_data:
                for key, value in requested_data.items():
                    if key == 'common_name':
                        filter_condition = "a.common_name = %s"
                    elif key == 'class_name':
                        filter_condition = "c.name = %s"
                    elif key == 'order_name':
                        filter_condition = "o.name = %s"
                    elif key == 'family_name':
                        filter_condition = "f.name = %s"
                    param = value
                    break

            if filter_condition:
                query += " WHERE " + filter_condition

            cursor.execute(query, (param,))

            rows = cursor.fetchall()

            if cursor.description is None:
                raise ValueError('No columns returned from the query')

            column_names = [desc[0] for desc in cursor.description]

            animals = [dict(zip(column_names, row)) for row in rows]

            if not animals:
                raise ValueError('Animal(s) not found from the given parameters')

            return animals

        except Exception as e:
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)
                
    def add_marker_data(self, data: Dict[str, Any]) -> Dict[str, str]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None

        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()

            conn.autocommit = False

            query = db_queries.ADD_MARKER
            cursor.execute(query, (
                data['mid'],
                data['marker_lat_lon'],
                data['marker_location'],
                data['marker_title'],
                data['marker_date_placed'],
                data['marker_placed_by_uid'],
                data['marker_status'],
                data['marker_animal_details'],
                data['marker_stats'],
            ))

            conn.commit()

            return {"message": "Data added successfully."}

        except psycopg2.Error as e:
            if conn:
                conn.rollback()
            return {"error": f"SQL Error: {str(e)}"}

        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)

    def get_marker_data(self, req_marker: str) -> Dict[str, Any]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None
    
        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()
    
            query = db_queries.GET_MARKER
    
            cursor.execute(query, (req_marker,))
    
            row = cursor.fetchone()
    
            if cursor.description is None:
                raise ValueError('No columns returned from the query')
    
            if row is None:
                raise LookupError('Marker not found from the given parameters')
    
            column_names = [desc[0] for desc in cursor.description]
            marker = dict(zip(column_names, row))
    
            return marker
    
        except Exception as e:
            raise e
    
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)
                
    def add_user_data(self, data: Dict[str, Any]) -> Dict[str, str]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None

        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()

            conn.autocommit = False

            query = db_queries.ADD_USER
            cursor.execute(query, (
                data['uid'],
                data['username'],
                data['email'],
                data['hashed_pw'],
                data['user_stats'],
            ))

            conn.commit()

            return {"message": "Data added successfully."}

        except psycopg2.Error as e:
            if conn:
                conn.rollback()
            return {"error": f"SQL Error: {str(e)}"}

        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)

    def get_user_data(self, req_user: str) -> Dict[str, Any]:
        """TEMPORARY PLACEHOLDER DOCSTRING!"""
        conn = None
        cursor = None
    
        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()
    
            query = db_queries.GET_USER
    
            cursor.execute(query, (req_user,))
    
            row = cursor.fetchone()
    
            if cursor.description is None:
                raise ValueError('No columns returned from the query')
    
            if row is None:
                raise LookupError('User not found from the given parameters')
    
            column_names = [desc[0] for desc in cursor.description]
            user = dict(zip(column_names, row))
    
            return user
    
        except Exception as e:
            raise e
    
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)