from src.database_manager import DatabaseManager
from src.person_service import PersonService
import pytest

@pytest.fixture(autouse=True, scope='function')
def person_service():
    db = DatabaseManager().initialize_database()
    db.create_tables()
    yield PersonService(db)
    db.drop_all_tables(with_all_data=True)
    
def create_2_persons(person_service):
    p1 = person_service.add_person('John', 'Smith')
    p2 = person_service.add_person('Mary', 'Cooper')
    return [p1, p2]

def test_add_person(person_service):
    persons = create_2_persons(person_service)
    person_service.add_person('Carl', 'Parker')

    assert person_service.count_persons() == len(persons) + 1

def test_remove_person(person_service):
    persons = create_2_persons(person_service)
    person_service.remove_person(persons[0].id)

    assert person_service.count_persons() == 1

def test_get_person_by_id(person_service):
    persons = create_2_persons(person_service)
    person = person_service.get_person_by_id(persons[0].id)

    assert persons[0].id== person.id
    assert persons[0].first_name == person.first_name
    assert persons[0].last_name == person.last_name

def test_list_all_persons(person_service):
    persons = create_2_persons(person_service)
    all_persons = person_service.list_all_persons()
    all_persons_ids = map(lambda x:x.id, all_persons)
    persons_ids = map(lambda x:x.id, persons)

    assert len(all_persons) == len(persons)
    assert all(person_id in persons_ids for person_id in all_persons_ids)
