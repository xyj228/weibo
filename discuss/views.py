from flask import request, redirect, render_template, Blueprint

from discuss.models import Discuss
from libs.orm import db

dcs_bp = Blueprint('disscuss', __name__, url_prefix='/discuss')
