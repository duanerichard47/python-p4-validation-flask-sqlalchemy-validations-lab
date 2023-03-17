from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number= db.Column(db.Integer(length=10))
    title = db.Column(db.String)     

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, CheckConstraint('length >=250'))
    summary = db.Column(db.String(length=250))
    category = db.Column(db.Boolean, CheckConstraint('(category == Fiction) or (category == Non_Fiction)'))

    @validates('title')
    def validate_title(self, key, title):
        valid_titles = ["Won't Believe", "Secret", "Top [number]", "Guess"]
        if title not in valid_titles:
            raise ValueError("Failed title validation")
        return title