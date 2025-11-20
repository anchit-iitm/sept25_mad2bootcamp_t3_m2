from backendjobs.worker import celery_app

@celery_app.task()
# @app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return x + y


@celery_app.task()
def hello():
    print("Hello, World!")
    return "Hello, World!"


@celery_app.task()
def find_person(id):
    from models import Person
    person = Person.query.get(id) # Person.query.filter_by(id=id).first()
    if person:
        return {"id": person.id, "name": person.name, "age": person.age}
    else:
        return {"error": "Person not found"}