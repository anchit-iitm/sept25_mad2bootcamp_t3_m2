from .import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Person {self.name}>' # Representation of the Person model, Person Anchit
    



    def formatter(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

    def get_by_id(user_id):
        # validations
        if not user_id:
            return None
        if not isinstance(user_id, int):
            return None
        if user_id <= 0:
            return None
        
        data = Person.query.get(user_id)
        return data.formatter() if data else None
    
    def get_all():
        return [user.formatter() for user in Person.query.all()]
    
    def create(name, age):
        # validations
        if not name or not isinstance(name, str):
            return None
        if not age or not isinstance(age, int) or age <= 0:
            return None
        
        new_user = Person(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return new_user.formatter()
    
    def update(user_id, name=None, age=None):
        # validations
        if not user_id or not isinstance(user_id, int) or user_id <= 0:
            return None
            
        user = Person.query.get(user_id)
        if user:
            if name:
                user.name = name
            if age:
                user.age = age
            db.session.commit()
        return user.formatter() if user else None

    def delete(user_id):
        # validations
        if not user_id or not isinstance(user_id, int) or user_id <= 0:
            return None

        user = Person.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user.formatter() if user else None
