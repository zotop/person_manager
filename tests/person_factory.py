from pony.orm import *
from mixer.backend.pony import mixer

class PersonFactory:

    def __init__(self, database):
        self.db = database

    @db_session
    def create(self):
        return mixer.blend(self.db.Person)

    @db_session
    def create_many(self, times):
      return [ self.create() for x in range(0, times) ]
