from flask import Flask

def create_app():

    init_app = Flask(__name__)

    from config import developmentConfig
    init_app.config.from_object(developmentConfig)

    from models import db
    db.init_app(init_app)


    from routes import bp_app
    init_app.register_blueprint(bp_app)

    from flask_security import Security
    from models import user_datastore
    Security(init_app, user_datastore)
    
    from flask_cors import CORS
    CORS(init_app)

    from caching import cache
    cache.init_app(init_app)

    from mailing import mail
    mail.init_app(init_app)

    return init_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)