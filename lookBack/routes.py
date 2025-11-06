from flask import render_template, request, redirect, url_for
from app import app

@app.route('/about')
def about():
    # with app.app_context():
    return "This is the About page of the LookBack App."


@app.route('/contact/add', methods=['GET', 'POST'])
def add_contact():
    # with app.app_context():
    from models import User, db
    if request.method == 'POST':
        new_user = User(name=request.form['name'], age=request.form['age'])
        db.session.add(new_user)
        db.session.commit()
        return redirect('/bp/contact')
    return render_template('add_contact.html')