from person_service import *
import pytest

@pytest.yield_fixture(autouse=True)
def run_around_tests():
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    yield

def test_add_person():
    PersonService().add_person('John', 'Smith')
    assert PersonService().count_persons() == 1

def test_remove_person():
    p1 = PersonService().add_person('John', 'Smith')
    p2 = PersonService().add_person('Mary', 'Cooper')
    PersonService().remove_person(p1.id)
    
    assert PersonService().count_persons() == 1
    
def test_get_person():
    p1 = PersonService().add_person('John', 'Smith')
    p2 = PersonService().add_person('Mary', 'Cooper')
    john = PersonService().get_person(p1.id)   
    
    assert john.id == p1.id
    assert john.first_name == p1.first_name
    assert john.last_name == p1.last_name
    
def test_list_all_persons():
    p1 = PersonService().add_person('John', 'Smith')
    p2 = PersonService().add_person('Mary', 'Cooper')
    all_persons = PersonService().list_all_persons()
    all_persons_ids = map(lambda x:x.id, all_persons)
    
    assert len(all_persons) == 2
    assert all(person_id in [p1.id, p2.id] for person_id in all_persons_ids)
    
    
        