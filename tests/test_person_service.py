from src.models import db
from src.person_service import PersonService
import pytest

def create_2_persons():
    p1 = PersonService().add_person('John', 'Smith')
    p2 = PersonService().add_person('Mary', 'Cooper')
    return [p1, p2]

@pytest.yield_fixture(autouse=True)
def run_around_tests():
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    yield

def test_add_person():
    create_2_persons()
    PersonService().add_person('Carl', 'Parker')

    assert PersonService().count_persons() == 3

def test_remove_person():
    persons = create_2_persons()
    PersonService().remove_person(persons[0].id)

    assert PersonService().count_persons() == 1

def test_get_person_by_id():
    persons = create_2_persons()
    person = PersonService().get_person_by_id(persons[0].id)

    assert persons[0].id== person.id
    assert persons[0].first_name == person.first_name
    assert persons[0].last_name == person.last_name

def test_list_all_persons():
    persons = create_2_persons()
    all_persons = PersonService().list_all_persons()
    all_persons_ids = map(lambda x:x.id, all_persons)
    persons_ids = map(lambda x:x.id, persons)

    assert len(all_persons) == len(persons)
    assert all(person_id in persons_ids for person_id in all_persons_ids)
