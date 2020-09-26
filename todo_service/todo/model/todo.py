from marshmallow import fields, Schema
from todo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    todo = db.relationship('Todo', backref='creator', lazy=True)

    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.todo = []

    def change_name(self, name):
        self.name = name
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.id

    @classmethod
    def get_user(cls):
        return cls.query.get(id)

    def add_todo(self, todo_query):
        todo = Todo(todo_query)
        self.todo.append(todo)
        db.session.commit()

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text(), nullable=False)
    owner = db.Column(db.String(225))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, data):
        self.id = data.get('id')
        self.task = data.get('task')
        self.owner = data.get('owner')
        self.user_id = data.get('user')

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.id

    @classmethod
    def get_task(cls, task_id):
        return cls.query.get(task_id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "task": self.task,
            "owner": self.owner,
            "user_id": self.user_id
        }


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    task = fields.String(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(dump_only=True)
    todos = fields.String(dump_only=True)
    task = fields.Nested(TodoSchema, only=["task"])
