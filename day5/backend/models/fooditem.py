from .import db

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<FoodItem {self.name}>'