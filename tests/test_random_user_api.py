from app.random_user_api import RandomUserApi
import pytest

def test_get_random_person():
    person = RandomUserApi().get_random_person()

    assert len(person['first_name']) > 0
    assert len(person['last_name']) > 0
    assert len(person['profile_picture_url']) > 0
    assert 'http' in person['profile_picture_url']
