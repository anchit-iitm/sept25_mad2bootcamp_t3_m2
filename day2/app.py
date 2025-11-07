from flask import Flask

def create_app():

    init_app = Flask(__name__)

    from config import developmentConfig
    init_app.config.from_object(developmentConfig)

    from models import db
    db.init_app(init_app)


    from routes import bp_app
    init_app.register_blueprint(bp_app)

    # optional
    from routes1 import api
    api.init_app(init_app)

    from flask_security import Security
    Security(init_app)
    
    return init_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)