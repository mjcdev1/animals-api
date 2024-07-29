from flask import request, jsonify
import os

def init_routes(app, db_ops):
    @app.route('/')
    def index():
        message = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>API Connected Successfully</title>
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

    @app.route('/add_animal_data', methods=['POST'])
    def add_animal_data():
        try: 
            api_key = request.args.get('api_key')
            data = request.json
            
            if not api_key or api_key != os.getenv('API_KEY'):
                    raise ValueError("API key is invalid or missing.")
            
            required_fields = [
                'common_name', 'class_name', 'order_name', 'family_name', 
                'species_name', 'scientific_name', 'conservation_status'
            ]
            
            missing_fields = [field for field in required_fields if not data.get(field)]
            
            if missing_fields:
                raise ValueError("The animal data is missing some required fields.")
            
            result = db_ops.add_animal_data(data)
            
            if 'error' in result:
                raise ValueError(result)
            
            return jsonify(result)
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 403
        except LookupError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": "An unexpected error occurred."}), 500

    @app.route('/get_animals', methods=['GET'])
    def get_animal():
        try:
            api_key = request.args.get('api_key')
            if not api_key or api_key != os.getenv('API_KEY'):
                raise ValueError("API key is invalid or missing.")
                
            requested_data = request.json
                
            animals = db_ops.get_animals_data(requested_data)
                
            if not animals:
                raise LookupError("Animal not found in database.")
                
            return jsonify(animals)
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 403
        except LookupError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": "An unexpected error occurred."}), 500