from todo.model.todo import User, Todo
from todo import db


def remove_todo(todo_id):
    todo = Todo.query.get(todo_id)
    print(todo)
    todo.query.filter(Todo.id == todo.id).delete()
    db.session.commit()
    return todo


class UserService:
    def __init__(self, creator_id):
        self.user = User.query.get(creator_id)

    def add_todo(self, data):
        todo = Todo(data)
        self.user.todo.append(todo)
        db.session.commit()
