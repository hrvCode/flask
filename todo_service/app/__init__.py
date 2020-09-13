from flask import Flask
from flask_sqlalchemy from SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from app import routes