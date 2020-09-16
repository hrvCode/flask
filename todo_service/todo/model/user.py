# from marshmallow import fields, Schema
# from todo import db
# from todo import TodoSchema


# class User(db.Model):
#     __tableName__: "User"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     todo = db.Relationship('Todo', backref="user", lazy="true")

#     def __init__(self, data):
#         self.id = data.get('id')
#         self.name = data.get('name')


#     def save():
#         db.session.add(self)
#         db.session.commit()
        
#         return self.id


#     @classmethod
#     def getUser(cls):
#         return cls.query.get(id)


# class UserSchema (Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.String(dump_only=True)
#     todos = fields.String(dump_only=True)
#     task = field.nested(TodoSchema, only=["task"])

