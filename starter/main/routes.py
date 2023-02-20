from flask import render_template
from starter.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    user = {'username': 'Bob'}
    return render_template('main/index.html', title='Home', user=user)