from flask import request, Blueprint, render_template, session
import datetime
from libs.orm import db
from product.models import Pro

pro_bp = Blueprint('pro', __name__, url_prefix='/product', template_folder='./templates')


@pro_bp.route('/')
def first():
    return render_template('myarticle.html')


@pro_bp.route('/create', methods=('POST', 'GET'))
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        text = request.form.get('article')
        date = datetime.datetime.now()
        try:
            Pro.query.filter_by(name=name).one()
        except Exception as e:
            pro = Pro()
            pro.name = name
            pro.article = text
            pro.date = date
            db.session.add(pro)
            db.session.commit()
            return render_template('rlt.html', pro=pro)
        else:
            return '文章名字重复，请更改'
    else:
        return render_template('create.html')


@pro_bp.route('/change', methods=('POST', 'GET'))
def change():
    if request.method == 'POST':
        name = request.form.get('name')
        article = request.form.get('article')
        try:
            Pro.query.filter_by(name=name).one()
        except Exception as e:
            return '文章不存在'
        else:
            pro = Pro.query.filter_by(name=name)
            pro.update({'article': article})
            db.session.commit()
            return '修改成功'
    else:
        return render_template('change.html')


@pro_bp.route('/delete', methods=('POST', 'GET'))
def delete():
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            Pro.query.filter_by(name=name).one()
        except Exception as e:
            return '文章不存在'
        else:
            pro = Pro.query.filter_by(name=name).one()
            db.session.delete(pro)
            db.session.commit()
            return '删除成功'
    else:
        return render_template('delete.html')


@pro_bp.route('/index', methods=('POST', 'GET'))
def index():
    uname = session['username']
    pro = Pro.query.all()
    return render_template('index.html', pro=pro, uname=uname)
