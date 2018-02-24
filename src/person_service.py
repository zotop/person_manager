from pony.orm import *

class PersonService:

    def __init__(self, database):
        self.db = database

    @db_session
    def add_person(self, first_name, last_name):
        return self.db.Person(first_name=first_name, last_name=last_name)

    @db_session
    def remove_person(self,person_id):
        self.db.Person[person_id].delete()

    @db_session
    def get_person_by_id(self, person_id):
        return self.db.Person.get(id=person_id)

    @db_session
    def list_all_persons(self):
        return self.db.Person.select()[:]

    @db_session
    def count_persons(self):
        return self.db.Person.select().count()
