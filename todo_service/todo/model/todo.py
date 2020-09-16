from marshmallow import fields, Schema
from todo import db

class User(db.Model):
    #__tableName__: "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    todo = db.relationship('Todo', backref='creator', lazy=True)

    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')


    def save(self):
        db.session.add(self)
        db.session.commit()
        
        return self.id


    @classmethod
    def getUser(cls):
        return cls.query.get(id)



class Todo (db.Model):
    # __tablename__  = "Todo"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text(), nullable=False)
    owner = db.Column(db.String(225))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, data):
        self.id = data.get('id')
        self.task = data.get('task')
        self.owner = data.get('owner')
        self.user_id = data.get('user_id')

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.id

    @classmethod
    def getTask(cls, id):
        return cls.query.get(id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "tsk": self.task,
            "owner": self.owner,
            "creator": self.creator
        }

class TodoSchema (Schema):
    id = fields.Int(dump_only=True)
    task = fields.String(dump_only=True)

class UserSchema (Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(dump_only=True)
    todos = fields.String(dump_only=True)
    task = fields.Nested(TodoSchema, only=["task"])




