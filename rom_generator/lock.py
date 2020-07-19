from rom_generator.generator import makeActor
import rom_generator.scriptFunctions as scripts

curKeyNumber = 511

def pickUpKey():
    return


def addKey(sprite, x, y):
    key = makeActor(sprite, x, y, animate = False)
    #key["startScript"].append()  Plan on disabling collisions here
    key["script"]
    key["script"].append(scripts.actorHide(actorId = key["spriteSheetId"]))
    key["script"].append(scripts.setTrue(variable = curKeyNumber))
    return key

def addLock(sprite, x, y):
    lock = makeActor(sprite, x, y, animate = False)
    trueCommands = [
        scripts.setFalse(variable = curKeyNumber),
        scripts.actorHide(actorId = lock["spriteSheetId"])
    ]
    lock["script"].append(scripts.ifTrue(variable = curKeyNumber))
    curKeyNumber = curKeyNumber - 1
    return lock
