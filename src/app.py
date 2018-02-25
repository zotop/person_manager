from flask import Flask, render_template, request, json
from os import environ
from person_api import person_api_blueprint

app = Flask(__name__)

app.register_blueprint(person_api_blueprint)

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = int(environ.get("PORT", 5000)))
