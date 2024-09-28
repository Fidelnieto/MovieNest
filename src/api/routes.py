"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import request, jsonify, Blueprint
from api.models import db, User, Todo
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# USERS endpoints
#-------------------------------------------------------
@api.route('/users', methods=['GET'])
def fetch_users():
    users = User.query.all()

    serialized_users = []
    for user in users:
        serialized_users.append(user.serialize())

    return jsonify(serialized_users)

@api.route('/users/<int:user_id>/todos', methods=['GET'])
def fetch_todos_of_an_user(user_id):
    todos_of_an_user = Todo.query.filter(Todo.user_id == user_id).all()

    serialized_todos = []
    for todo in todos_of_an_user:
        serialized_todos.append(todo.serialize())

    return jsonify(serialized_todos)

@api.route('/users', methods=['POST'])
def create_user():
    request_data = request.get_json()
    name = request_data.get('name')
    quote = request_data.get('quote')

    new_user = User(name=name, quote=quote)
    db.session.add(new_user)
    db.session.commit()

    return f"New user with id: {new_user.id} created"

@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)

    db.session.delete(user_to_delete)
    db.session.commit()

    return f"Deleting user with id: {user_id}"
#-------------------------------------------------------

#TODOS endpoints
@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo_to_delete = Todo.query.get(todo_id)

    db.session.delete(todo_to_delete)
    db.session.commit()

    return f"Deleting todo with id: {todo_id}"

@api.route('/todos', methods=['POST'])
def create_todo():
    request_data = request.get_json()
    content = request_data.get('content')
    completed = request_data.get('completed')
    user_id = request_data.get('user_id')

    new_todo = Todo(content=content, completed=completed, user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()

    return f"New todo with id: {new_todo.id} created"

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    request_data = request.get_json()
    todo_to_update = Todo.query.get(todo_id)

    if 'content' in request_data:
        todo_to_update.content = request_data.get('content')
    if 'completed' in request_data:
        todo_to_update.completed = request_data.get('completed')
    if 'user_id' in request_data:
        todo_to_update.user_id = request_data.get('user_id')

    db.session.commit()
    return f"Todo with id: {todo_id} Updated"
