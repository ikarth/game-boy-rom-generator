import scriptFunctions as scripts
import variable as var

#set position probably has to move to set position to value

def setUpScene(scene, weapon, player, enemy = []):
    scene["script"].append(scripts.actorHide(weapon["id"]))
    script = []
    playerX = var.getOpenVariable()
    playerY = var.getOpenVariable()
    script.append(scripts.actorGetPosition(actorId = player, vectorX = playerX, vectorY = playerY))
    script.append(scripts.actorInvoke(actorId = weapon["id"]))
    scene["script"].append(scripts.setInputScript(scripts = script))

    weaponScript = []
    enemyLoc = [] #max of 8 enemies
    for e in enemy:
        enemyX = var.getOpenVariable()
        enemyY = var.getOpenVariable()
        enemyLoc.append(enemyX)
        enemyLoc.append(enemyY)
        weaponScript.append(scripts.actorGetPosition(actorId = e["id"], vectorX = enemyX, vectorY = enemyY))
    
    weaponScript.append(scripts.actorSetPositionToValue(actorId = weapon["id"], vectorX = playerX, vectorY = playerY))
    weaponScript.append(scripts.actorShow(actorId = weapon["id"]))

    temp = scripts.ifActorDirection(player, "right", "False", [scripts.actorMoveRelative(weapon["id"], 2, 0)], [])

    temp = scripts.ifActorDirection(player, "left", "False", [scripts.actorMoveRelative(weapon["id"], -2, 0)], [temp])

    temp = scripts.ifActorDirection(player, "up", "False", [scripts.actorMoveRelative(weapon["id"], 0, -2)], [temp])

    temp = scripts.ifActorDirection(player, "down", "False", [scripts.actorMoveRelative(weapon["id"], 0, 2)], [temp])

    weaponScript.append(temp)
    weaponX = var.getOpenVariable()
    weaponY = var.getOpenVariable()
    weaponScript.append(scripts.actorSetPositionToValue(weapon["id"], vectorX = weaponX, vectorY = weaponY)) #THIS MUCH BE CHANGED

    curIndex = 0
    offset = var.getOpenVariable()
    for e in enemy:
        temp = scripts.ifValueCompare(vectorX = offset, operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = [])

        temp = scripts.ifValueCompare(vectorX = offset, operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = [scripts.variableMath(vectorX = offset, other = "var", vectorY = enemyLoc[curIndex]), 
                scripts.variableMath(vectorX = offset, operation = "add", other = "val", vectorY = offset), temp])

        temp = scripts.ifValueCompare(vectorX = offset, operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = [scripts.variableMath(vectorX = offset, other = "var", vectorY = enemyLoc[curIndex]), 
                scripts.variableMath(vectorX = offset, operation = "add", other = "val", vectorY = offset), temp])

        #weaponScript.append(ifValueCompare(vectorX = enemyLoc[curIndex + 1], operator = "==", vectorY = weaponY, trueCommands = [scripts.ifValueCompare(vectorX = enemyLoc[curIndex], operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = [])], falseCommands = [temp]))    

        

    weaponScript.append(scripts.wait("0.1"))
    weaponScript.append(scripts.actorHide(weapon["id"]))


    weapon["script"] = weaponScript

