from flask import Flask, request, abort, jsonify
import json
import psycopg2
from psycopg2 import pool
from typing import Any, Dict
from dotenv import load_dotenv
import os
import db_queries

load_dotenv('database.env')

class Database:
    def __init__(self):
        self.database_name = os.getenv('DATABASE_NAME')
        self.database_host = os.getenv('DATABASE_HOST')
        self.database_user = os.getenv('DATABASE_USER')
        self.database_pw = os.getenv('DATABASE_PW')
        self.database_port = os.getenv('DATABASE_PORT')
        self.db_pool = pool.SimpleConnectionPool(
                1,  # Min connections 
                10,  # Max connections
                dbname=self.database_name,
                user=self.database_user,
                password=self.database_pw,
                host=self.database_host,
                port=self.database_port
            )
            
        print(self.database_name)
            
    def db_connect(self):
        conn = self.db_pool.getconn()
        return conn
        
    def db_close(self, conn):
        self.db_pool.putconn(conn)

    
class DBOps:
    def __init__(self, database):
        self.database = database
        
    def add_animal_data(self, data):
        conn = None
        cursor = None
        
        try:
            conn = self.database.db_connect()
            cursor = conn.cursor()
            
            conn.autocommit = False
            
            query = db_queries.ADD_CLASS
            cursor.execute(query, (data['class_name'],))
            
            query = query = db_queries.ADD_ORDER
            cursor.execute(query, (data['order_name'], data['class_name']))
            
            query = db_queries.ADD_FAMILY
            cursor.execute(query, (data['family_name'], data['order_name']))
            
            query = db_queries.ADD_SPECIES
            cursor.execute(query, (data['species_name'], data['family_name']))
            
            if data['subspecies_name']:
                query = db_queries.ADD_SUBSPECIES
                cursor.execute(query, (data['subspecies_name'], data['species_name']))
                
            
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
                return {"error": "Unique constraint violation: Duplicate record exists."}
            return {"error": f"SQL Error: {str(e)}"}
    
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.database.db_close(conn)
    
    def get_animals_data(self, requested_data):
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


        
class API:
    def __init__(self, app, db_ops):
        self.app = app
        self.db_ops = db_ops
        self.api_key = os.getenv('API_KEY')  
        self.api_routes()
        
    def api_routes(self):
        @self.app.route('/')
        def index():
            message = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>API Connected Succesfully</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    ul { line-height: 1.6; }
                    h1 { color: #333; }
                </style>
            </head>
            <body>
                <h1>API Connected</h1>
                <h3><u>API endpoints:</u></h3>
                <ul>
                    <li>
                        <b>/animals</b>
                        <ul>
                            <li>Returns a specific animal or a list of animals from the database</li>
                            <li>Arguments:</li>
                            <ul>
                                <li>api_key: Your API key <b>*REQUIRED*</b></li>
                                <li>com: The common name of an animal <b>*(Note: If you use this argument, you cannot use any other filter argument)*</b></li>
                                <li>cla: A class of animals <b>*(Note: If you use this argument, you cannot use any other filter argument)*</b></li>
                                <li>ord: An order of animals <b>*(Note: If you use this argument, you cannot use any other filter argument)*</b></li>
                                <li>fam: A family of animals <b>*(Note: If you use this argument, you cannot use any other filter argument)*</b></li>
                            </ul>
                        </ul>
                    </li>
                </ul>
            </body>
            </html>
            '''
            return message
            
        @self.app.route('/add_animal_data', methods=['POST'])
        def add_animal_data():
            try: 
                api_key = request.args.get('api_key')
                data = request.json
                
                if not api_key or api_key != self.api_key:
                        raise ValueError("API key is invalid or missing.")
                
                required_fields = [
                    'common_name', 'class_name', 'order_name', 'family_name', 
                    'species_name', 'scientific_name', 'conservation_status'
                ]
                
                missing_fields = [field for field in required_fields if not data.get(field)]
                
                if missing_fields:
                    raise ValueError("The animal data is missing some required fields.")
                
                result = self.db_ops.add_animal_data(data)
                
                if 'error' in result:
                    raise ValueError(result)
                
                return jsonify(result)
                
            except ValueError as e:
                return jsonify({"error": str(e)}), 403
            except LookupError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": "An unexpected error occurred."}), 500

        @self.app.route('/get_animals', methods=['GET'])
        def get_animal():
            try:
                api_key = request.args.get('api_key')
                if not api_key or api_key != self.api_key:
                    raise ValueError("API key is invalid or missing.")
                    
                requested_data = request.json
                    
                animals = self.db_ops.get_animals_data(requested_data)
                    
                if not animals:
                    raise LookupError("Animal not found in database.")
                    
                return jsonify(animals)
                
            except ValueError as e:
                return jsonify({"error": str(e)}), 403
            except LookupError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": "An unexpected error occurred."}), 500

app = Flask(__name__)
app.json.sort_keys = False
    
database = Database()
db_ops = DBOps(database)
api = API(app, db_ops)

if __name__ == '__main__':
    
    app.run(debug=True)
