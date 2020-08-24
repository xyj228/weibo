from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db

# 初始化app
app = Flask(__name__)
app.secret_key = r'sdas&%tsgdy&^&dt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Xyj970228..@localhost/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 初始化manager
manager = Manager(app)

# 初始化db和migrate
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def home():
    '''首页'''
    return 'Hello'


if __name__ == '__main__':
    manager.run()
