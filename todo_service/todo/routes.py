from todo import app
from flask import make_response, request, jsonify
from todo.model.todo import Todo, User
from service.user_service import UserService, remove_todo


@app.route('/', methods=['get'])
def index():
    # skicka frontend
    return make_response('hello', 200)


@app.route('/api/todo/', methods=['get'])
def get_all():
    return jsonify([i.serialize for i in Todo.query.all()])


@app.route('/api/user/todo/<int:user_id>', methods=['get'])
def get_all_todos_by_user():
    return jsonify([i.serialize for i in Todo.query.all()])


@app.route('/api/todo/<int:todo_id>', methods=['get'])
def get_todo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'


@app.route('/api/todo/', methods=['post'])
def create_todo():
    if request.method == 'POST':
        # move to todo_service
        req = request.get_json()
        user_service = UserService(req['creator'])
        user_service.add_todo(req)
        return make_response(f"no")


@app.route('/api/todo/<int:todo_id>', methods=['put'])
def update_todo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'


@app.route('/api/todo/<int:user_id>', methods=['delete'])
def delete_todo(user_id):
    print(request.method)
    if request.method == 'DELETE':
        req = request.get_json()
        todo = remove_todo(req['todoId'])
        return make_response(f'DELETED: {todo.task} BY USER:{user_id}', 200)


#API USERS

@app.route('/api/user', methods=['post'])
def create_user():
    if request.method == 'POST':
        # move to User service
        user_data = request.get_json()
        user = User(user_data)
        user_id = user.save()
        print(user_id)
        return make_response(f"you just made a user with id: {user_id}")
