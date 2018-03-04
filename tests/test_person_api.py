from app.app import app
from app.database_manager import DatabaseManager
from app.person_service import PersonService
import json
import pytest
from tests.person_factory import PersonFactory

@pytest.fixture(scope='session')
def test_client():
    return app.test_client()

@pytest.fixture(scope='session')
def db():
    return DatabaseManager().initialize_database()

@pytest.fixture(scope='session')
def person_service(db):
    return PersonService(db)

@pytest.fixture(scope='session')
def person_factory(db):
    return PersonFactory(db)

@pytest.fixture(autouse=True, scope='function')
def run_around_tests(db):
    db.create_tables()
    yield
    db.drop_all_tables(with_all_data=True)

#POST Add Person
def test_add_new_person(test_client):
    person = json.dumps(dict(first_name='John', last_name='Parker'))
    response = test_client.post('/api/persons', data=person, content_type='application/json')
    json_response = json.loads(response.get_data())

    assert response.status_code == 201
    assert json_response.get('first_name') == 'John'
    assert json_response.get('last_name') == 'Parker'
    assert json_response.get('id') != None

#DELETE Person
def test_delete_person(test_client, person_service, person_factory):
    person = person_factory.create()
    response = test_client.delete('/api/persons/' + str(person.id))

    assert response.status_code == 204
    assert person_service.count_persons() == 0

def test_delete_person_that_is_not_found(test_client):
    response = test_client.delete('/api/persons/20')
    assert response.status_code == 404

# GET Person
def test_get_person(test_client, person_factory):
    persons = person_factory.create_many(2)
    response = test_client.get('/api/persons/' + str(persons[0].id))
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert json_response.get('first_name') == persons[0].first_name
    assert json_response.get('last_name') ==  persons[0].last_name
    assert json_response.get('id') != None

def test_get_person_that_is_not_found(test_client):
    response = test_client.get('/api/persons/1')
    assert response.status_code == 404

# GET List all Persons
def test_list_all_persons(test_client, person_factory):
    persons = person_factory.create_many(2)
    response = test_client.get('/api/persons/list')
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(json_response) == 2

def test_list_all_persons_when_there_is_none(test_client):
    response = test_client.get('/api/persons/list')
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(json_response) == 0

# POST Import random Person
#TODO: mock response to avoid randomuser api call
def test_import_random_person(test_client):
    response = test_client.post('/api/persons/import/random')
    json_response = json.loads(response.get_data())

    assert response.status_code == 201
    assert len(json_response.get('first_name')) > 0
    assert len(json_response.get('last_name')) > 0
    assert json_response.get('id') != None
