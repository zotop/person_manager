from src.app import app
from src.database_manager import DatabaseManager
from src.person_service import PersonService
import json
import pytest

@pytest.fixture(scope='session')
def test_client():
    return app.test_client()

@pytest.fixture(scope='session')
def db():
    return DatabaseManager().initialize_database()

@pytest.fixture(scope='session')
def person_service(db):
    return PersonService(db)

@pytest.fixture(autouse=True, scope='function')
def run_around_tests(db):
    db.create_tables()
    yield
    db.drop_all_tables(with_all_data=True)

def test_add_new_person(test_client, person_service):
    person = json.dumps(dict(first_name='John', last_name='Parker'))
    response = test_client.post('/api/person', data=person, content_type='application/json')
    json_response = json.loads(response.get_data())

    assert response.status_code == 201
    assert json_response.get('first_name') == 'John'
    assert json_response.get('last_name') == 'Parker'
    assert json_response.get('id') != None

def test_delete_person(test_client, person_service):
    person = person_service.add_person(first_name='Mary', last_name='Goldman')
    response = test_client.delete('/api/person/' + str(person.id))

    assert response.status_code == 204
    assert person_service.count_persons() == 0
