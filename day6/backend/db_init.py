from app import create_app
from models import db, user_datastore

app = create_app()


def create_roles():
    roles = ['admin', 'manager', 'user']
    for role in roles:
        user_datastore.find_or_create_role(name=role)
    db.session.commit()
    return "Roles created.", roles

def create_admin():
    from security import hash_password
    hashed_password, status = hash_password("admin123")
    if not user_datastore.find_user(id=1): # User.query.find_by(id=1).first()
        user_datastore.create_user(email="admin@abc.com", password=hashed_password, roles=['admin'])
        db.session.commit()
        return "Admin user created.", True
    return "Admin user already exists.", False

with app.app_context():
    db.drop_all()
    db.create_all()
    message, roles = create_roles()
    if message == "Roles created.":
        message, created = create_admin()
