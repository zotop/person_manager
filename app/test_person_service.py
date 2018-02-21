from person_service import *


def test_add_person():
    PersonService().add_person('John', 'Smith')
    PersonService().add_person('Mary', 'Cooper')
    assert PersonService().count_persons() == 2
