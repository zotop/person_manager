from flask import Flask
from os import environ
from person_api import person_api_blueprint

app = Flask(__name__)

app.register_blueprint(person_api_blueprint)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = int(environ.get("PORT", 5000)))