from todo.model.todo import User, Todo

from todo import db


class TodoService:
    def __init__(self):
        self.todo: None
        self.user: None

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
    def get_todo(self, todo_id):
        self.todo = Todo.query.get(todo_id)
        if not self.todo:
            print(self.todo)
        self.user = User.query.get(self.todo.user_id)
        return {"user": self.user, "todo": self.todo}