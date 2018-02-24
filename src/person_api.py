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

@person_api_blueprint.route('/api/person/<int:person_id>', methods=['DELETE'])
def remove_person(person_id):
    person_service.remove_person(person_id)
    return ('', 204)


@person_api_blueprint.route('/api/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = person_service.get_person_by_id(person_id)
    response = jsonify(person.to_dict())
    response.status_code = 200
    return response

@person_api_blueprint.route('/api/person/list', methods=['GET'])
def list_all_persons():
    all_persons = person_service.list_all_persons()
    all_persons = map(lambda x:x.to_dict(), all_persons)
    response = jsonify(all_persons)
    response.status_code = 200
    return response
