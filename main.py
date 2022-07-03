import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'first name': 'Andy',
                       'last name': 'Wu'})


if __name__ == "__main__":
    app.run()
