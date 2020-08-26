from flask import Flask, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp
from user.models import User
from product.views import pro_bp
from product.models import Pro
from discuss.views import dcs_bp
from discuss.models import Discuss

# 初始化app
app = Flask(__name__)
app.secret_key = r'sdas&%tsgdy&^&dt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Xyj970228..@localhost/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(pro_bp)
app.register_blueprint(dcs_bp)

# 初始化manager
manager = Manager(app)

# 初始化db和migrate
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def home():

    return render_template('home.html')



if __name__ == '__main__':
    print(app.url_map)
    manager.run()
