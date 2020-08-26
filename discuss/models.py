from libs.orm import db


class Discuss():
    __tablename__ = 'discuss'

    uname = db.Column(db.String(10))
    words = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)


def to():
    pass


def back():
    pass


def watch():
    pass
