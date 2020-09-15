from todo import app
from flask import make_response
from flask import request
from todo.model.todo import Todo

@app.route('/', methods=['get'])
def index():
    # skicka frontend
    return make_response('hello', 200)


@app.route('/api/todo/', methods=['get'])
def getAll():
    fromDb = Todo.getAllTasks()
    for todo in fromDb:
        print(todo)
   # return make_response(todoData)


@app.route('/api/todo/<int:post_id>', methods=['get'])
def getTodo(post_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'


@app.route('/api/todo/', methods=['post'])
def createTodo():
    if request.method == 'POST':
        content = request.get_json()
        em = Todo(content)
        id = em.save()
        print(content)
        return make_response("Id of todo", id)



@app.route('/api/todo/<int:post_id>',  methods=['put'])
def updateTodo(post_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'


@app.route('/api/todo/<int:post_id>', methods=['delete'])
def deleteTodo(post_id):
    # getTodo(post_id) // hämtar från dbn
    return f'todo id {post_id}'
