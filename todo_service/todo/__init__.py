from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresUser:postgresPassword@192.168.10.108:5432/todoDatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
from todo.model import todo
db.create_all()

from todo import routes
