import uuid
import copy

def makeElement():
    element = {}
    element["id"] = str(uuid.uuid4())
    return copy.deepcopy(element)

