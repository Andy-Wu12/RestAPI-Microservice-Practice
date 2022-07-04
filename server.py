import json
import pymongo
from flask import Flask, jsonify, request

app = Flask(__name__)

# Local mongodb connection
client = pymongo.MongoClient('localhost', 27017)
db = client.flask_rest_project

@app.route('/users', methods=['GET'])
def getPeople():
    user_collection = db.users
    docs_cursor = user_collection.find()
    data = []

    # Convert oid to string to allow for jsonify to work properly
    for doc in docs_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)

    return jsonify(data)


# UIDs should be auto-generated, usually done by database with some sort of AUTO_INCREMENT
# Bash script automatically sets every uid to -1 for now, until I get database set up
@app.route('/users', methods=['POST'])
def setPerson():
    db.users.insert(request.get_json())
    return '', 204

if __name__ == "__main__":
    # debug=True allows for live server changes everytime the server code is updated
    app.run(debug=True)
