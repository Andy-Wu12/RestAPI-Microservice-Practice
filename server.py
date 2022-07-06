import json
import pymongo
from flask import Flask, jsonify, request, abort
from bson import ObjectId

app = Flask(__name__)

# Local mongodb connection
client = pymongo.MongoClient('localhost', 27017)
db = client.flask_rest_project

# Use to generate unique user id
# This should be in application server, but will be here until I create it
num_users = db.users.count_documents({})

@app.route('/users', methods=['GET'])
def getPeople():
    user_collection = db.users
    data = []

    # Get all query parameters.
    # Currently only handles filtering by fields separated by &
    query_dict = {}
    for param, value in request.args.items():
        query_dict[param] = value

    docs_cursor = user_collection.find(query_dict)

    # Convert oid to string to allow for jsonify to work properly
    for doc in docs_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)

    return jsonify(data)

@app.route('/users/<int:uid>', methods=['GET'])
def getPerson(uid):
    user_data = db.users.find_one({"uid": uid})

    if user_data:
        user_data['_id'] = str(user_data['_id'])
        return jsonify(user_data)

    return jsonify({'Error': 'No user with that id was found!'})

@app.route('/users', methods=['POST'])
def addPerson():
    global num_users

    json_data = request.get_json()
    num_users += 1
    json_data['uid'] = num_users

    db.users.insert_one(json_data)
    return '', 204

@app.route('/users', methods=['PUT'])
def updatePerson():
    # uid uniquely identifies user, so query db with that to get correct document
    updated_data = request.get_json()
    user_id = updated_data['uid']

    db.users.update_one({'uid': user_id}, {'$set': updated_data})
    return '', 204

if __name__ == "__main__":
    # debug=True allows for live server changes everytime the server code is updated
    app.run(debug=True)
