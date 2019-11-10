from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def add_user(self, _name, _words):
        new_user = User(name=_name, words=_words)
        db.session.add(new_user)
        db.session.commit()

    def get_all_users(self):
        return User.query.all()
    
    def __repr__(self):
        user_obj = {
            'name': self.name,
        }
        return ' self.name