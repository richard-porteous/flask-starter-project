from flask import render_template
from starter.main import bp
from flask_login import current_user, login_required

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = {'username': current_user.username}
    return render_template('main/index.html', title='Home', user=user)
