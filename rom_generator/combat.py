import scriptFunctions as scripts

def setUpScene(scene, weapon, player):
    scene["scripts"].append(scripts.actorHide(weapon["id"]))
    script = []
    script.append(scripts.actorGetPosition(actorId = player["id"], vectorX = "0", vectorY = "1"))
    script.append(scripts.actorInvoke(actorId = weapon["id"]))
    scene["scripts"].append(scripts.setInputScript(scripts = script))