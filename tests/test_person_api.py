from src.app import app 
import json
import pytest

@pytest.fixture(scope='session')
def test_client():
    return app.test_client()
    
def test_add_new_person(test_client):
    person = json.dumps(dict(first_name='John', last_name='Parker'))
    response = test_client.post('/api/person', data=person, content_type='application/json')
    json_response = json.loads(response.get_data())

    assert response.status_code == 201
    assert json_response.get('first_name') == 'John'
    assert json_response.get('last_name') == 'Parker'
    assert json_response.get('id') != None
    