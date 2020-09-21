from todo.model.todo import User, Todo

from todo import db


class TodoService:
    @staticmethod
    def remove_todo(data):
        user = User.query.get(data['userId'])
        delete_todo = Todo.query.get(data['todoId'])
        if [delete_todo.id in user.todo == delete_todo.id]:
            delete_todo.query.filter(Todo.id == delete_todo.id).delete()
            db.session.commit()
            return delete_todo

    @staticmethod
    def add_todo(data):
        user = User.query.get(data['userId'])
        user.add_todo(data)

    @staticmethod
    def get_todo(todo_id):
        todo = Todo.query.get(todo_id)
        return todo.serialize