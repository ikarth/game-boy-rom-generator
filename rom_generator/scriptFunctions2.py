from rom_generator.utilities import makeElement

'''
This is just a temporary place to put methods that don't seem to be generated yet
'''

def disableCollisions(actorId = "player"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_COLLISIONS_DISABLE"
    element["args"] = {
        "actorId": actorId
    }
    return element