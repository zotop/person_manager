from src.database_manager import DatabaseManager
from src.person_service import PersonService
from tests.person_factory import PersonFactory
import pytest

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

def test_add_person(person_service, person_factory):
    persons = person_factory.create_many(2)
    person_service.add_person('Carl', 'Parker')

    assert person_service.count_persons() == len(persons) + 1

def test_remove_person(person_service, person_factory):
    persons = person_factory.create_many(2)
    person_service.remove_person(persons[0].id)

    assert person_service.count_persons() == 1

def test_get_person_by_id(person_service, person_factory):
    persons = person_factory.create_many(2)
    person = person_service.get_person_by_id(persons[0].id)

    assert persons[0].id== person.id
    assert persons[0].first_name == person.first_name
    assert persons[0].last_name == person.last_name

def test_list_all_persons(person_service, person_factory):
    persons = person_factory.create_many(2)
    all_persons = person_service.list_all_persons()
    all_persons_ids = map(lambda x:x.id, all_persons)
    persons_ids = map(lambda x:x.id, persons)

    assert len(all_persons) == len(persons)
    assert all(person_id in persons_ids for person_id in all_persons_ids)
