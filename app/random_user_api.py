import requests

API_ENDPOINT = "https://randomuser.me/api"

class RandomUserApi:

    def get_random_person(self):
        response = requests.get(API_ENDPOINT)
        user_json = response.json()
        name = user_json['results'][0]['name']
        picture = user_json['results'][0]['picture']
        person_dict = {}
        person_dict['first_name'] = name['first'].title()
        person_dict['last_name'] = name['last'].title()
        person_dict['profile_picture_url'] = picture['large']
        return person_dict
