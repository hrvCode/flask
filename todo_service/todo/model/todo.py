from marshmallow import fields, Schema
from todo import db

class Todo (db.Model):
    __tablename__  = "task"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text())
    owner = db.Column(db.String(255))

    def __init__(self, data):
        self.id = data.get('id')
        self.task = data.get('task')
        self.owner = data.get('owner')

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.id

    @classmethod
    def getTask(cls, id):
        return cls.query.get(id)

    @classmethod
    def getAllTasks(cls):
        k = db.session.query(cls).all()
        print(k)
        return k


class TodoSchema (Schema):
    id = fields.Int(dump_only=True)
    task = fields.String(dump_only=True)
    owner = fields.String(dump_only=True)
