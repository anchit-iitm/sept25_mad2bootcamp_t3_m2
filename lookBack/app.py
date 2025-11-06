from flask import Flask
from models import db
from route import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lookback.sqlite3'

db.init_app(app)
app.register_blueprint(bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    print('hello')
    return "Welcome to the LookBack App!"

from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)