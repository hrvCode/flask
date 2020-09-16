from todo import app
from flask import make_response, request, jsonify
from todo.model.todo import Todo, User
import json

@app.route('/', methods=['get'])
def index():
    # skicka frontend
    return make_response('hello', 200)


@app.route('/api/todo/', methods=['get'])
def getAll():
    return jsonify([i.serialize for i in Todo.query.all()])

@app.route('/api/user/todo/<int:user_id>', methods=['get'])
def getAllTodosByUserId():
    return jsonify([i.serialize for i in Todo.query.all()])


@app.route('/api/todo/<int:todo_id>', methods=['get'])
def getTodo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'


@app.route('/api/todo/', methods=['post'])
def createTodo():
    if request.method == 'POST':
        #move to todoservice
        content = request.get_json()
        todo = Todo(content)
        user = User.query.get(1)
        user.todo.append(todo)
        user.save()
        return make_response(f"{user.name} added to do Task: '{todo.task}' shall be executed by: {todo.owner}")



@app.route('/api/todo/<int:todo_id>',  methods=['put'])
def updateTodo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'


@app.route('/api/todo/<int:post_id>', methods=['delete'])
def deleteTodo(todo_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {todo_id}'





## API USERS

@app.route('/api/user', methods=['post'])
def createUser():

    if request.method == 'POST':
        #move to User service
        userData = request.get_json()
        user = User(userData)
        user_id = user.save()
        print(user_id)
        return make_response(f"you just made a user with id: {user_id}") 
