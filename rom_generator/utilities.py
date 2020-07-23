import uuid
import copy

### Create a basic GBS element, with a unique ID
def makeElement():
    element = {}
    element["id"] = str(uuid.uuid4())
    return copy.deepcopy(element)
