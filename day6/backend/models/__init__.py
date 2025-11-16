from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore

db = SQLAlchemy()

from .vehicles import Vehicle
from .user import Person
from .fooditem import FoodItem
from .security import User, Role, RolesUsers

user_datastore = SQLAlchemyUserDatastore(db, User, Role)