import rom_generator.script_functions as scripts
import rom_generator.variable as var

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
    weaponScript.append(scripts.actorGetPosition(weapon["id"], vectorX = weaponX, vectorY = weaponY)) #THIS MUCH BE CHANGED

    curIndex = 0
    offset = var.getOpenVariable()
    for e in enemy:
        temp = scripts.ifValueCompare(vectorX = offset, operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = [])

        offsetCommand = [scripts.variableMath(vectorX = offset, other = "var", vectorY = enemyLoc[curIndex]),
                scripts.variableMath(vectorX = offset, operation = "sub", other = "val", vectorY = 1), temp] #check subtract works  



        temp = scripts.ifValueCompare(vectorX = offset, operator = "==", vectorY = weaponX, trueCommands = [scripts.actorHide(e["id"])], falseCommands = offsetCommand)


        offsetCommand = [scripts.variableMath(vectorX = offset, other = "var", vectorY = enemyLoc[curIndex]),
                scripts.variableMath(vectorX = offset, operation = "add", other = "val", vectorY = 1), temp]

        temp2 = scripts.ifValueCompare(vectorX = enemyLoc[curIndex], operator = "==", vectorY = weaponX, 
                trueCommands = [scripts.actorHide(e["id"])], falseCommands = offsetCommand)

        temp = scripts.ifValueCompare(vectorX = enemyLoc[curIndex + 1], operator = "==", vectorY = offset, 
                trueCommands = [scripts.actorHide(e["id"])], falseCommands = [])

        temp = scripts.ifValueCompare(vectorX = enemyLoc[curIndex], operator = "==", vectorY = weaponX, 
                trueCommands = [temp], falseCommands = [])

        offsetCom = [scripts.variableMath(vectorX = offset, other = "var", vectorY = enemyLoc[curIndex + 1]),
                scripts.variableMath(vectorX = offset, operation = "add", other = "val", vectorY = 1), temp]

        temp3 = scripts.ifValueCompare(vectorX = enemyLoc[curIndex + 1], operator = "==", vectorY = weaponY, __collapseElse = False, trueCommands = [temp2], falseCommands = offsetCom)
        curIndex += 2
        weaponScript.append(temp3)



    #weaponScript.append(scripts.wait("0.1"))
    weaponScript.append(scripts.actorHide(weapon["id"]))


    weapon["script"] = weaponScript
