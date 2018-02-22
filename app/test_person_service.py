from person_service import *
import pytest

@pytest.yield_fixture(autouse=True)
def run_around_tests():
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    yield


def test_add_person():
    PersonService().add_person('John', 'Smith')
    PersonService().add_person('Mary', 'Cooper')
    assert PersonService().count_persons() == 2


def test_remove_person():
    p1 = PersonService().add_person('John', 'Smith')
    p2 = PersonService().add_person('Mary', 'Cooper')
    PersonService().remove_person(p2.id)
    assert PersonService().count_persons() == 1