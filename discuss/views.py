from flask import request, redirect, render_template, Blueprint, session

import datetime
from discuss.models import Discuss
from libs.orm import db
from discuss.models import Back
from product.models import Pro

dcs_bp = Blueprint('disscuss', __name__, url_prefix='/discuss', template_folder='./templates')


@dcs_bp.route('/to', methods=('POST', 'GET'))
def to():
    if request.method == 'POST':
        username = session['username']
        discuss = request.form.get('discuss')
        dis = Discuss()
        dis.uname = username
        dis.date = datetime.datetime.now()
        dis.words = discuss
        db.session.add(dis)
        db.session.commit()
        return '评论成功'
    else:
        return render_template('to.html')


@dcs_bp.route('/bk', methods=('POST', 'GET'))
def bk():
    if request.method == 'POST':
        pass
    else:
        return render_template('bk.html')


@dcs_bp.route('/watch')
def watch():
    username=session['username']
    dis = Discuss.query.filter_by(uname=username)
    return render_template('watch.html', dis=dis)
