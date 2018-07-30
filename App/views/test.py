from flask import Blueprint,render_template,request
from App.extensions import db
from App.models import User
import random
test=Blueprint('test',__name__)
@test.route('/create_table/')
def create_table():
    return 'hhh'