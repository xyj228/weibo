from libs.orm import db


class Pro(db.Model):
    __tablename__ = 'pro'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    uname = db.Column(db.String(10))
    article = db.Column(db.Text, default='请写点什么')
    date = db.Column(db.Date)