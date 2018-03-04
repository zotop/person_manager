# Person Manager

* Adds, lists, views, deletes a person using Flask framework, PonyORM and Sqlite.
* Imports and stores random persons from https://randomuser.me/ API.

## Running locally

Install Virtualenv, then: 
```
pip install -r requirements.txt
python app/app.py
```

Or via docker-compose: 
```
  docker-compose build
  docker-compose up
```
  
This will start a local development server on http://0.0.0.0:5000/  


## Running tests 

To run all the tests: ```py.test tests```

### Heroku App

Travis runs the tests and builds a container image that is pushed to Heroku's Container Registry.

https://lit-meadow-88864.herokuapp.com/
