from todo import app
from flask import make_response, request, jsonify
from todo.model.todo import Todo, User
from service.user_service import UserService
from service.todo_service import TodoService
from flask_cors import CORS

CORS(app, resources=r'/api/*')


@app.route('/', methods=['get'])
def index():
    # skicka frontend
    return make_response('hello', 200)


@app.route('/api/todo', methods=['get'])
def get_all():
    if request.method == 'GET':
        # get all todos
        return jsonify([i.serialize for i in Todo.query.all()])
    # create todo
    if request.method == 'POST':
        req = request.get_json()
        todo_service = TodoService()
        todo_service.add_todo(req)
        return make_response(f"no")


@app.route('/api/user/todo', methods=['get'])
def get_all_todos_by_user():
    # get all todos from specific user
    req = request.get_json()
    todos = UserService.get_all_todos_by_user(req)
    return jsonify([todo.serialize for todo in todos])


@app.route('/api/todo/<int:todo_id>', methods=['get', 'delete'])
def get_todo(todo_id):
    # get specific todo
    if request.method == "GET":
        todo_service = TodoService
        data = todo_service.get_todo(todo_service, todo_id)

        if not data['todo'].serialize:
            return make_response(jsonify(None))
        else:
            return jsonify({
                "user": data["user"].serialize,
                "todos": [data["todo"].serialize]
            })

    if request.method == "PUT":
        return f'todo id {todo_id}'

    # delete todo
    if request.method == 'DELETE':
        req = request.get_json()
        todo = TodoService.remove_todo(req)
        return make_response(f'DELETED TODO: {todo.task}:', 200)


# API USERS
@app.route('/api/user', methods=['get', 'post'])
def get_all_users():
    # get all users
    if request.method == 'GET':
        user = UserService.get_all_user()
        return make_response(jsonify(user), 200)
    # Create user
    if request.method == 'POST':
        user_data = request.get_json()
        user_id = UserService.add_user(user_data)
        return make_response(f"you just made a user with id:{user_id}", 200)


@app.route('/api/user/<int:user_id>', methods=['get', 'put', 'delete'])
def get_user(user_id):
    if request.method == "GET":
        # get user
        user = UserService.get_user(user_id)
        return make_response(jsonify(user.serialize), 200)
        # update user
    if request.method == 'PUT':
        req = request.get_json()
        user = UserService.change_my_name(req, user_id)
        return user.serialize
        # delete user
    if request.method == 'DELETE':
        req = request.get_json()
        user = UserService.delete_user(req['userId'])
        return make_response(f'DELETED USER: {user}:', 200)
