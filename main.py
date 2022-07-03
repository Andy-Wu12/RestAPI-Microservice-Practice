import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {'firstName': 'Andy', 'lastName': 'Wu'},
    {'firstName': 'April', 'lastName': 'May'},
    {'firstName': 'Crystal', 'lastName': 'Waters'}
]

@app.route('/users', methods=['GET'])
def getPeople():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def setPerson():
    users.append(request.get_json())
    return '', 204

if __name__ == "__main__":
    # debug=True allows for live server changes everytime the server code is updated
    app.run(debug=True)
