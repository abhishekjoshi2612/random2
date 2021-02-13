from server import db
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    caption = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120),  nullable=False)
    db.UniqueConstraint(name,caption,url)
    def __init__(self,name,caption,url):
        self.name = name
        self.caption = caption
        self.url = url
    def __repr__(self):
        return '<User %r>' % self.name

