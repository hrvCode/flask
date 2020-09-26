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
    # get all todos
    return jsonify([i.serialize for i in Todo.query.all()])


@app.route('/api/user/<int:user_id>/todo', methods=['get'])
def get_all_todos_by_user(user_id):
    # get all todos from specific user
    todos = UserService.get_all_todos_by_user(user_id)
    return jsonify([todo.serialize for todo in todos])


@app.route('/api/todo/<int:todo_id>', methods=['get'])
def get_todo(todo_id):

    todo_service = TodoService
    data = todo_service.get_todo(todo_service,todo_id)

    if not todo_service.serialize:
        return make_response(jsonify(None))
    else:
        return jsonify({
            "user": data["user"].serialize,
            "todos": [data["todo"].serialize]
        })


@app.route('/api/todo/', methods=['post'])
def create_todo():
    # create todo
    if request.method == 'POST':
        req = request.get_json()
        todo_service = TodoService()
        todo_service.add_todo(req)
        return make_response(f"no")


@app.route('/api/todo/<int:todo_id>', methods=['put'])
def update_todo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'


@app.route('/api/todo/', methods=['delete'])
def delete_todo():
    # delete todo
    if request.method == 'DELETE':
        req = request.get_json()
        todo = TodoService.remove_todo(req)
        return make_response(f'DELETED TODO: {todo.task}:', 200)

# API USERS


@app.route('/api/user/<int:user_id>', methods=['get'])
def get_update_delete_user(user_id):
    if request.method == "GET":
        user = UserService.get_user(user_id)
        return make_response(jsonify(user), 200)
    if request.method == "PUT":
        pass

    if request.method == "DELETE":


@app.route('/api/user', methods=['post,delete'])
def get_all_create_user():
    # create user
    if request.method == 'POST':
        user_data = request.get_json()
        user_id = UserService.add_user(user_data)
        return make_response(f"you just made a user with id:{user_id}")
    if request.method == 'GET':
        return [i.serialize for i in Todo.query.all()]