from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename=':memory:')

class Person(db.Entity):
    first_name = Required(str)
    last_name = Required(str)

db.generate_mapping(create_tables=True)
