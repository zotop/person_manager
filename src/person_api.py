from flask import Blueprint, jsonify, request
from database_manager import DatabaseManager
from person_service import PersonService

person_api_blueprint = Blueprint('person_api', __name__)
db = DatabaseManager().initialize_database()
person_service = PersonService(db)

@person_api_blueprint.route('/api/person', methods=['POST'])
def add_new_person():
    json = request.get_json()
    new_person = person_service.add_person(first_name=json['first_name'], last_name=json['last_name'])
    response = jsonify(new_person.to_dict())
    response.status_code = 201
    return response