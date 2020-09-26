from todo.model.todo import User, Todo
from todo import db


class UserService:

    @staticmethod
    def add_user(user_data):
        new_user = User(user_data)
        return new_user.save();

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        return user.serialize

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
    def get_all_todos_by_user(user_id):
        user = User.query.get(user_id)
        return user.todo

    @staticmethod
    def delete_user(user_id):
        return User.query.delete


