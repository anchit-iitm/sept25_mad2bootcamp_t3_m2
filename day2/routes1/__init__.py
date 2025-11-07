from flask_restful import Api

api = Api(prefix='/api/v1')

from .general import home, about
api.add_resource(home, '/')
api.add_resource(about, '/about')

from .users import users
api.add_resource(users, '/users')