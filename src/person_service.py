from .models import *

class PersonService():

    @db_session
    def add_person(self, first_name, last_name):
        return Person(first_name=first_name, last_name=last_name)

    @db_session
    def remove_person(self,person_id):
        Person[person_id].delete()

    @db_session
    def get_person_by_id(self, person_id):
        return Person.get(id=person_id)

    @db_session
    def list_all_persons(self):
        return Person.select()[:]

    @db_session
    def count_persons(self):
        return Person.select().count()
