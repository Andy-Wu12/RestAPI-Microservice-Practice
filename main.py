import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample starting data
users = [
    {'uid': 1, 'favoriteColor': 'red', 'firstName': 'Andy', 'lastName': 'Wu'},
    {'uid': 2, 'favoriteColor': 'yellow', 'firstName': 'April', 'lastName': 'May'},
    {'uid': 3, 'favoriteColor': 'blue', 'firstName': 'Crystal', 'lastName': 'Waters'}
]

@app.route('/users', methods=['GET'])
def getPeople():
    return jsonify(users)

# UIDs should be auto-generated, usually done by database with some sort of AUTO_INCREMENT
# Bash script automatically sets every uid to -1 for now, until I get database set up
@app.route('/users', methods=['POST'])
def setPerson():
    users.append(request.get_json())
    return '', 204

if __name__ == "__main__":
    # debug=True allows for live server changes everytime the server code is updated
    app.run(debug=True)
