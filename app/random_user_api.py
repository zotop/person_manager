import requests

API_ENDPOINT = "https://randomuser.me/api"

class RandomUserApi:

    def get_random_person(self):
        response = requests.get(API_ENDPOINT)
        user_json = response.json()
        name = user_json['results'][0]['name']
        first_name = name['first'].title()
        last_name = name['last'].title()
        person_dict = dict(first_name=first_name,last_name=last_name)
        return person_dict
