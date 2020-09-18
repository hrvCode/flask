from todo import app
from flask import make_response, request, jsonify
from todo.model.todo import Todo, User
from service.user_service import UserService
from service.todo_service import TodoService


@app.route('/', methods=['get'])
def index():
    # skicka frontend
    return make_response('hello', 200)


@app.route('/api/todo/', methods=['get'])
def get_all():
    # get all todos
    return jsonify([i.serialize for i in Todo.query.all()])


@app.route('/api/user/todo/<int:user_id>', methods=['get'])
def get_all_todos_by_user(user_id):
    # get all todos from specific user
    todos = UserService.get_all_todos_by_user(user_id)
    return jsonify([todo.serialize for todo in todos])


@app.route('/api/todo/<int:todo_id>', methods=['get'])
def get_todo(todo_id):
    # get todo
    return f'todo id {todo_id}'


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

@app.route('/api/user', methods=['post'])
def create_user():
    # create user
    if request.method == 'POST':
        user_data = request.get_json()
        user_id = UserService.add_user(user_data)
        return make_response(f"you just made a user with id:{user_id}")
