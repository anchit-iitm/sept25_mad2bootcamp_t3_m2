from backendjobs.worker import celery_app

@celery_app.task()
def add(x, y):
    return x + y


@celery_app.task()
def hello():
    print("Hello, World!")
    return "Hello, World!"


@celery_app.task()
def find_person(id):
    from models import Person
    person = Person.query.get(id)
    if person:
        return {"id": person.id, "name": person.name, "age": person.age}
    else:
        return {"error": "Person not found"}