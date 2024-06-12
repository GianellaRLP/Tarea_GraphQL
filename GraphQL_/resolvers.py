
def resolve_hello(obj, info):
    return "Hello, world!"

def resolve_greeting(obj, info, name):
    return f"Hello, {name}!"

people_db = {
    "1": {"id": "1", "name": "Alice", "age": 30},
    "2": {"id": "2", "name": "Bob", "age": 25},
}

def resolve_getPerson(obj, info, id):
    return people_db.get(id)
