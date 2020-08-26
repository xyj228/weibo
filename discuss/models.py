from libs.orm import db


class Discuss(db.Model):
    __tablename__ = 'discuss'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(10))
    pname = db.Column(db.String(10))
    words = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)


class Back(db.Model):
    __tablename__ = 'back'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(10))
    backwords = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)
