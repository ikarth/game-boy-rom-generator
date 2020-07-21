from utilities import makeElement

### Create a basic GBS element, with a unique ID
def end():
    element = makeElement()
    element["command"] = "EVENT_END"
    element["args"] = {
    }
    return element

def stop():
    element = makeElement()
    element["command"] = "EVENT_STOP"
    element["args"] = {
    }
    return element

def wait(time = "0.5"):
    element = makeElement()
    element["command"] = "EVENT_WAIT"
    element["args"] = {
        "time": time,
    }
    return element

def switchScene(sceneId = "498cfdcf-3000-453f-9b52-fe5d8d81cac2", x = "7", y = "6", direction = "", fadeSpeed = "2"):
    element = makeElement()
    element["command"] = "EVENT_SWITCH_SCENE"
    element["args"] = {
        "sceneId": sceneId,
        "x": x,
        "y": y,
        "direction": direction,
        "fadeSpeed": fadeSpeed,
    }
    return element

def startBattle():
    element = makeElement()
    element["command"] = "EVENT_START_BATTLE"
    element["args"] = {
    }
    return element

def returnToTitle():
    element = makeElement()
    element["command"] = "EVENT_RETURN_TO_TITLE"
    element["args"] = {
    }
    return element

def scenePushState():
    element = makeElement()
    element["command"] = "EVENT_SCENE_PUSH_STATE"
    element["args"] = {
    }
    return element

def scenePopState(fadeSpeed = "2"):
    element = makeElement()
    element["command"] = "EVENT_SCENE_POP_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element

def sceneResetState():
    element = makeElement()
    element["command"] = "EVENT_SCENE_RESET_STATE"
    element["args"] = {
    }
    return element

def scenePopAllState(fadeSpeed = "2"):
    element = makeElement()
    element["command"] = "EVENT_SCENE_POP_ALL_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element

def loadData():
    element = makeElement()
    element["command"] = "EVENT_LOAD_DATA"
    element["args"] = {
    }
    return element

def saveData():
    element = makeElement()
    element["command"] = "EVENT_SAVE_DATA"
    element["args"] = {
    }
    return element

def clearData():
    element = makeElement()
    element["command"] = "EVENT_CLEAR_DATA"
    element["args"] = {
    }
    return element

def ifTrue(variable = "L0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_TRUE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifFalse(variable = "L0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_FALSE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifValue(variable = "L3", operator = ">", comparator = "2", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_VALUE"
    element["args"] = {
        "variable": variable,
        "operator": operator,
        "comparator": comparator,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifValueCompare(vectorX = "6", operator = "==", vectorY = "3", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_VALUE_COMPARE"
    element["args"] = {
        "vectorX": vectorX,
        "operator": operator,
        "vectorY": vectorY,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifInput(input = "['a', 'b']", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_INPUT"
    element["args"] = {
        "input": input,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifActorDirection(actorId = "player", direction = "up", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_ACTOR_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifSavedData(__collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_SAVED_DATA"
    element["args"] = {
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifActorAtPosition(actorId = "player", x = "0", y = "0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_ACTOR_AT_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def setTrue(variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_SET_TRUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def setFalse(variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_SET_FALSE"
    element["args"] = {
        "variable": variable,
    }
    return element

def choice(variable = "L0", trueText = "", falseText = ""):
    element = makeElement()
    element["command"] = "EVENT_CHOICE"
    element["args"] = {
        "variable": variable,
        "trueText": trueText,
        "falseText": falseText,
    }
    return element

def resetVariables():
    element = makeElement()
    element["command"] = "EVENT_RESET_VARIABLES"
    element["args"] = {
    }
    return element

def loop(loopCommand):
    element = makeElement()
    element["command"] = "EVENT_LOOP"
    element["args"] = {
    }
    loopCommand.add(end())
    element["children"] = {
        "true": loopCommand
    }
    return element

def group(groupCommands):
    element = makeElement()
    element["command"] = "EVENT_GROUP"
    element["args"] = {
    }
    groupCommands.add(end())
    element["children"] = {
        "true": groupCommands
    }
    return element

def menu(variable = "L0", items = "2", option1 = "", option2 = "", option3 = "", option4 = "", option5 = "", option6 = "", option7 = "", option8 = "", cancelOnB = "True", layout = "dialogue"):
    element = makeElement()
    element["command"] = "EVENT_MENU"
    element["args"] = {
        "variable": variable,
        "items": items,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "option4": option4,
        "option5": option5,
        "option6": option6,
        "option7": option7,
        "option8": option8,
        "cancelOnB": cancelOnB,
        "layout": layout,
    }
    return element

def comment(text = ""):
    element = makeElement()
    element["command"] = "EVENT_COMMENT"
    element["args"] = {
        "text": text,
    }
    return element
    
def setInputScript(input = "b",scripts=[]):
    element = makeElement()
    element["command"] = "EVENT_SET_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    scripts.append(end())
    element["children"] = {
        "true": scripts
    }
    return element

def setBackgroundScript():
    element = makeElement()
    element["command"] = "EVENT_SET_BACKGROUND_SCRIPT"
    element["args"] = {
    }
    return element

def removeInputScript(input = "['b']"):
    element = makeElement()
    element["command"] = "EVENT_REMOVE_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    return element

def variableMath(vectorX = "L0", operation = "set", other = "true", vectorY = "L0", value = "1", minValue = "0", maxValue = "255"):
    element = makeElement()
    element["command"] = "EVENT_VARIABLE_MATH"
    element["args"] = {
        "vectorX": vectorX,
        "operation": operation,
        "other": other,
        "vectorY": vectorY,
        "value": value,
        "minValue": minValue,
        "maxValue": maxValue,
    }
    return element

def setValue(variable = "L0", value = "0"):
    element = makeElement()
    element["command"] = "EVENT_SET_VALUE"
    element["args"] = {
        "variable": variable,
        "value": value,
    }
    return element

def setRandomValue():
    element = makeElement()
    element["command"] = "EVENT_SET_RANDOM_VALUE"
    element["args"] = {
    }
    return element

def incValue(variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_INC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def decValue(variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_DEC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def mathAdd():
    element = makeElement()
    element["command"] = "EVENT_MATH_ADD"
    element["args"] = {
    }
    return element

def mathSub():
    element = makeElement()
    element["command"] = "EVENT_MATH_SUB"
    element["args"] = {
    }
    return element

def mathMul():
    element = makeElement()
    element["command"] = "EVENT_MATH_MUL"
    element["args"] = {
    }
    return element

def mathDiv():
    element = makeElement()
    element["command"] = "EVENT_MATH_DIV"
    element["args"] = {
    }
    return element

def mathMod():
    element = makeElement()
    element["command"] = "EVENT_MATH_MOD"
    element["args"] = {
    }
    return element

def mathAddValue():
    element = makeElement()
    element["command"] = "EVENT_MATH_ADD_VALUE"
    element["args"] = {
    }
    return element

def mathSubValue():
    element = makeElement()
    element["command"] = "EVENT_MATH_SUB_VALUE"
    element["args"] = {
    }
    return element

def mathMulValue():
    element = makeElement()
    element["command"] = "EVENT_MATH_MUL_VALUE"
    element["args"] = {
    }
    return element

def mathDivValue():
    element = makeElement()
    element["command"] = "EVENT_MATH_DIV_VALUE"
    element["args"] = {
    }
    return element

def mathModValue():
    element = makeElement()
    element["command"] = "EVENT_MATH_MOD_VALUE"
    element["args"] = {
    }
    return element

def copyValue():
    element = makeElement()
    element["command"] = "EVENT_COPY_VALUE"
    element["args"] = {
    }
    return element

def setFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["command"] = "EVENT_SET_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def addFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["command"] = "EVENT_ADD_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def clearFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["command"] = "EVENT_CLEAR_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def ifFlagsCompare(variable = "L0", flag = "1", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["command"] = "EVENT_IF_FLAGS_COMPARE"
    element["args"] = {
        "variable": variable,
        "flag": flag,
        "__collapseElse": __collapseElse,
    }
    trueCommands.append(end())
    falseCommands.append(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def awaitInput(input = "['a', 'b']"):
    element = makeElement()
    element["command"] = "EVENT_AWAIT_INPUT"
    element["args"] = {
        "input": input,
    }
    return element

def text(text = "'push", avatarId = ""):
    element = makeElement()
    element["command"] = "EVENT_TEXT"
    element["args"] = {
        "text": text,
        "avatarId": avatarId,
    }
    return element

def textSetAnimationSpeed(speedIn = "1", speedOut = "1", speed = "1"):
    element = makeElement()
    element["command"] = "EVENT_TEXT_SET_ANIMATION_SPEED"
    element["args"] = {
        "speedIn": speedIn,
        "speedOut": speedOut,
        "speed": speed,
    }
    return element

def actorSetDirection(actorId = "player", direction = "up"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element

def actorSetDirectionToValue(actorId = "player", variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_DIRECTION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element

def actorSetPosition(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorSetPositionRelative(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorMoveRelative(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorMoveTo():
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_TO"
    element["args"] = {
    }
    return element

def actorPush(doContinue = "False"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_PUSH"
    element["args"] = {
        "continue": doContinue,
    }
    return element

def actorSetAnimationSpeed(actorId = "player", speed = "3"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_ANIMATION_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element

def actorSetMovementSpeed(actorId = "player", speed = "1"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_MOVEMENT_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element

def actorEmote(actorId = "player", emoteId = "0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_EMOTE"
    element["args"] = {
        "actorId": actorId,
        "emoteId": emoteId,
    }
    return element

def playerSetSprite(spriteSheetId = "468ef314-e09e-42e2-8778-99e1331e8beb"):
    element = makeElement()
    element["command"] = "EVENT_PLAYER_SET_SPRITE"
    element["args"] = {
        "spriteSheetId": spriteSheetId,
    }
    return element

def actorGetPosition(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_GET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorGetDirection(actorId = "player", direction = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_GET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element

def actorSetPositionToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorMoveToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorInvoke(actorId = "82444b20-65df-436a-b1c1-191aacf2258d"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_INVOKE"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def actorSetFrame(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", frame = "0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_FRAME"
    element["args"] = {
        "actorId": actorId,
        "frame": frame,
    }
    return element

def actorSetFrameToValue(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", variable = "L0"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_FRAME_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element

def cameraMoveTo(x = "0", y = "0", speed = "0"):
    element = makeElement()
    element["command"] = "EVENT_CAMERA_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element

def cameraLock(speed = "0"):
    element = makeElement()
    element["command"] = "EVENT_CAMERA_LOCK"
    element["args"] = {
        "speed": speed,
    }
    return element

def cameraShake(time = "0.5"):
    element = makeElement()
    element["command"] = "EVENT_CAMERA_SHAKE"
    element["args"] = {
        "time": time,
    }
    return element

def fadeOut(speed = "2"):
    element = makeElement()
    element["command"] = "EVENT_FADE_OUT"
    element["args"] = {
        "speed": speed,
    }
    return element

def fadeIn(speed = "2"):
    element = makeElement()
    element["command"] = "EVENT_FADE_IN"
    element["args"] = {
        "speed": speed,
    }
    return element

def showSprites():
    element = makeElement()
    element["command"] = "EVENT_SHOW_SPRITES"
    element["args"] = {
    }
    return element

def hideSprites():
    element = makeElement()
    element["command"] = "EVENT_HIDE_SPRITES"
    element["args"] = {
    }
    return element

def actorShow(actorId = "player"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SHOW"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def actorHide(actorId = "player"):
    element = makeElement()
    element["command"] = "EVENT_ACTOR_HIDE"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def overlayShow(color = "black", x = "0", y = "0"):
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_SHOW"
    element["args"] = {
        "color": color,
        "x": x,
        "y": y,
    }
    return element

def overlayHide():
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_HIDE"
    element["args"] = {
    }
    return element

def overlayMoveTo(x = "0", y = "0", speed = "1"):
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element

def musicPlay(musicId = "56622189-8327-4a64-bd29-2fbcf243c97e", loop = "True"):
    element = makeElement()
    element["command"] = "EVENT_MUSIC_PLAY"
    element["args"] = {
        "musicId": musicId,
        "loop": loop,
    }
    return element

def musicStop():
    element = makeElement()
    element["command"] = "EVENT_MUSIC_STOP"
    element["args"] = {
    }
    return element

def soundPlayBeep():
    element = makeElement()
    element["command"] = "EVENT_SOUND_PLAY_BEEP"
    element["args"] = {
    }
    return element

def callCustomEvent(customEventId = "4bf11658-2bb2-4e79-ad96-22577c9a8353", __name = "Custom Event 1"):
    element = makeElement()
    element["command"] = "EVENT_CALL_CUSTOM_EVENT"
    element["args"] = {
        "customEventId": customEventId,
        "__name": __name,
    }
    return element