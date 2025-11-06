from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/bp')

@bp.route('/about') # http://localhost:8080/bp/about
def about():
    return "This is the About page of the LookBack App. hey from the blueprint"

@bp.route('/contact')
def contact():
    from models import User
    users = User.query.all()

    message = 1
    if not users:
        message = 0
    return render_template('contact.html', html_users=users, message=message)