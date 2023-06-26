from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

state_objects = storage.all(State)
print("State objects dictionary: {}".format(state_objects))

if state_objects:
    first_state_id = list(state_objects.values())[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
