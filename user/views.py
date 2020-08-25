from flask import Blueprint, url_for
from flask import request, session
from flask import render_template
from flask import redirect

from libs.orm import db
from user.models import User


user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='./templates')



@user_bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('password')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        city = request.form.get('city')
        try:
            User.query.filter_by(username=name).one()
        except Exception as e:
            user = User()
            user.username = name
            user.password = pwd
            user.phone = phone
            user.gender = gender
            user.city = city
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return '该邮箱已注册，请直接登录'
    else:
        return render_template('./register.html')


@user_bp.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('password')
        try:
            user_info = User.query.filter_by(username=name).one()
        except Exception as e:
            return '用户未注册'
        else:
            if user_info.password != pwd:
                return '密码不正确'
            else:
                session['username'] = name
                return render_template('result.html', name=name)
    else:
        return render_template('./login.html')


@user_bp.route('/info')
def info():
    name = session.get('username')
    user = User.query.filter_by(username=name).one()
    return render_template('./info.html', user=user)
