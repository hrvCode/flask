from app import app
from flask import make_response
from markupsafe import escape 

@app.route('/', methods=['get'])
def index():
    #skicka frontend
    return make_response('hello',200)

@app.route('/todo', methods=['get'])
def todo():
    return "hello, todo!"

@app.route('/api/todo/', methods=['get'])
def getAll():
    #getTodos()
    pass

@app.route('/todo/<int:post_id>', methods=['get'])
def getTodo(post_id):
    #getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'

@app.route('/api/todo/', methods=['post'])
def createTodo():
    #createTodo()
    pass

@app.route('/todo/<int:post_id>',  methods=['put'])
def updateTodo(post_id):
    #getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'

@app.route('/todo/<int:post_id>', methods=['delete'])
def deleteTodo(post_id):
    #getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'