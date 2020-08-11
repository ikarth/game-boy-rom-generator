# Generated methods for scripts
from rom_generator.utilities import makeElement


# EVENT_END
def end():
    """
    Generated method for the GBS script action EVENT_END.

    """
    element = makeElement()
    element["command"] = "EVENT_END"
    return element


# EVENT_STOP
def stop():
    """
    Generated method for the GBS script action EVENT_STOP.

    """
    element = makeElement()
    element["command"] = "EVENT_STOP"
    return element


# EVENT_WAIT
def wait(time = "0.5"):
    """
    Generated method for the GBS script action EVENT_WAIT.

    time: float with a default value of "0.5"
    """
    element = makeElement()
    element["command"] = "EVENT_WAIT"
    element["args"] = {
        "time": time,
    }
    return element


# EVENT_SWITCH_SCENE
def switchScene(sceneId = "498cfdcf-3000-453f-9b52-fe5d8d81cac2", x = "7", y = "6", direction = "", fadeSpeed = "2"):
    """
    Generated method for the GBS script action EVENT_SWITCH_SCENE.

    sceneId: str with a default value of "498cfdcf-3000-453f-9b52-fe5d8d81cac2"
    x: int with a default value of "7"
    y: int with a default value of "6"
    direction: str with a default value of ""
    fadeSpeed: str with a default value of "2"
    """
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


# EVENT_START_BATTLE
def startBattle():
    """
    Generated method for the GBS script action EVENT_START_BATTLE.

    """
    element = makeElement()
    element["command"] = "EVENT_START_BATTLE"
    return element


# EVENT_RETURN_TO_TITLE
def returnToTitle():
    """
    Generated method for the GBS script action EVENT_RETURN_TO_TITLE.

    """
    element = makeElement()
    element["command"] = "EVENT_RETURN_TO_TITLE"
    return element


# EVENT_SCENE_PUSH_STATE
def scenePushState():
    """
    Generated method for the GBS script action EVENT_SCENE_PUSH_STATE.

    """
    element = makeElement()
    element["command"] = "EVENT_SCENE_PUSH_STATE"
    element["args"] = {
    }
    return element


# EVENT_SCENE_POP_STATE
def scenePopState(fadeSpeed = "2"):
    """
    Generated method for the GBS script action EVENT_SCENE_POP_STATE.

    fadeSpeed: str with a default value of "2"
    """
    element = makeElement()
    element["command"] = "EVENT_SCENE_POP_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element


# EVENT_SCENE_RESET_STATE
def sceneResetState():
    """
    Generated method for the GBS script action EVENT_SCENE_RESET_STATE.

    """
    element = makeElement()
    element["command"] = "EVENT_SCENE_RESET_STATE"
    return element


# EVENT_SCENE_POP_ALL_STATE
def scenePopAllState(fadeSpeed = "2"):
    """
    Generated method for the GBS script action EVENT_SCENE_POP_ALL_STATE.

    fadeSpeed: str with a default value of "2"
    """
    element = makeElement()
    element["command"] = "EVENT_SCENE_POP_ALL_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element


# EVENT_LOAD_DATA
def loadData():
    """
    Generated method for the GBS script action EVENT_LOAD_DATA.

    """
    element = makeElement()
    element["command"] = "EVENT_LOAD_DATA"
    element["args"] = {
    }
    return element


# EVENT_SAVE_DATA
def saveData():
    """
    Generated method for the GBS script action EVENT_SAVE_DATA.

    """
    element = makeElement()
    element["command"] = "EVENT_SAVE_DATA"
    return element


# EVENT_CLEAR_DATA
def clearData():
    """
    Generated method for the GBS script action EVENT_CLEAR_DATA.

    """
    element = makeElement()
    element["command"] = "EVENT_CLEAR_DATA"
    return element


# EVENT_IF_TRUE
def ifTrue(variable = "L0", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_TRUE.

    variable: str with a default value of "L0"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_TRUE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_FALSE
def ifFalse(variable = "L0", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_FALSE.

    variable: str with a default value of "L0"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_FALSE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_VALUE
def ifValue(variable = "L3", operator = ">", comparator = "2", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_VALUE.

    variable: str with a default value of "L3"
    operator: str with a default value of ">"
    comparator: int with a default value of "2"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_VALUE"
    element["args"] = {
        "variable": variable,
        "operator": operator,
        "comparator": comparator,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_VALUE_COMPARE
def ifValueCompare(vectorX = "6", operator = "==", vectorY = "3", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_VALUE_COMPARE.

    vectorX: str with a default value of "6"
    operator: str with a default value of "=="
    vectorY: str with a default value of "3"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_VALUE_COMPARE"
    element["args"] = {
        "vectorX": vectorX,
        "operator": operator,
        "vectorY": vectorY,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_INPUT
def ifInput(input = "['a', 'b']", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_INPUT.

    input: list with a default value of "['a', 'b']"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_INPUT"
    element["args"] = {
        "input": input,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_ACTOR_DIRECTION
def ifActorDirection(actorId = "player", direction = "up", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_ACTOR_DIRECTION.

    actorId: str with a default value of "player"
    direction: str with a default value of "up"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_ACTOR_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_SAVED_DATA
def ifSavedData(__collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_SAVED_DATA.

    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_SAVED_DATA"
    element["args"] = {
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_IF_ACTOR_AT_POSITION
def ifActorAtPosition(actorId = "player", x = "0", y = "0", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_ACTOR_AT_POSITION.

    actorId: str with a default value of "player"
    x: int with a default value of "0"
    y: int with a default value of "0"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_ACTOR_AT_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_SET_TRUE
def setTrue(variable = "L0"):
    """
    Generated method for the GBS script action EVENT_SET_TRUE.

    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_SET_TRUE"
    element["args"] = {
        "variable": variable,
    }
    return element


# EVENT_SET_FALSE
def setFalse(variable = "L0"):
    """
    Generated method for the GBS script action EVENT_SET_FALSE.

    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_SET_FALSE"
    element["args"] = {
        "variable": variable,
    }
    return element


# EVENT_CHOICE
def choice(variable = "L0", trueText = "", falseText = ""):
    """
    Generated method for the GBS script action EVENT_CHOICE.

    variable: str with a default value of "L0"
    trueText: str with a default value of ""
    falseText: str with a default value of ""
    """
    element = makeElement()
    element["command"] = "EVENT_CHOICE"
    element["args"] = {
        "variable": variable,
        "trueText": trueText,
        "falseText": falseText,
    }
    return element


# EVENT_RESET_VARIABLES
def resetVariables():
    """
    Generated method for the GBS script action EVENT_RESET_VARIABLES.

    """
    element = makeElement()
    element["command"] = "EVENT_RESET_VARIABLES"
    return element


# EVENT_LOOP
def loop(children = {'true': []}):
    """
    Generated method for the GBS script action EVENT_LOOP.

    """
    element = makeElement()
    element["command"] = "EVENT_LOOP"
    element["args"] = {
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_GROUP
def group(children = {'true': []}):
    """
    Generated method for the GBS script action EVENT_GROUP.

    """
    element = makeElement()
    element["command"] = "EVENT_GROUP"
    element["args"] = {
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_MENU
def menu(variable = "L0", items = "2", option1 = "", option2 = "", option3 = "", option4 = "", option5 = "", option6 = "", option7 = "", option8 = "", cancelOnB = "True", layout = "dialogue"):
    """
    Generated method for the GBS script action EVENT_MENU.

    variable: str with a default value of "L0"
    items: int with a default value of "2"
    option1: str with a default value of ""
    option2: str with a default value of ""
    option3: str with a default value of ""
    option4: str with a default value of ""
    option5: str with a default value of ""
    option6: str with a default value of ""
    option7: str with a default value of ""
    option8: str with a default value of ""
    cancelOnB: bool with a default value of "True"
    layout: str with a default value of "dialogue"
    """
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


# EVENT_COMMENT
def comment(text = ""):
    """
    Generated method for the GBS script action EVENT_COMMENT.

    text: str with a default value of ""
    """
    element = makeElement()
    element["command"] = "EVENT_COMMENT"
    element["args"] = {
        "text": text,
    }
    return element


# EVENT_SET_INPUT_SCRIPT
def setInputScript(input = "b", children = {'true': []}):
    """
    Generated method for the GBS script action EVENT_SET_INPUT_SCRIPT.

    input: str with a default value of "b"
    """
    element = makeElement()
    element["command"] = "EVENT_SET_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_SET_BACKGROUND_SCRIPT
def setBackgroundScript():
    """
    Generated method for the GBS script action EVENT_SET_BACKGROUND_SCRIPT.

    """
    element = makeElement()
    element["command"] = "EVENT_SET_BACKGROUND_SCRIPT"
    return element


# EVENT_REMOVE_INPUT_SCRIPT
def removeInputScript(input = "['b']"):
    """
    Generated method for the GBS script action EVENT_REMOVE_INPUT_SCRIPT.

    input: list with a default value of "['b']"
    """
    element = makeElement()
    element["command"] = "EVENT_REMOVE_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    return element


# EVENT_VARIABLE_MATH
def variableMath(vectorX = "L0", operation = "set", other = "true", vectorY = "L0", value = "1", minValue = "0", maxValue = "255"):
    """
    Generated method for the GBS script action EVENT_VARIABLE_MATH.

    vectorX: str with a default value of "L0"
    operation: str with a default value of "set"
    other: str with a default value of "true"
    vectorY: str with a default value of "L0"
    value: str with a default value of "1"
    minValue: str with a default value of "0"
    maxValue: str with a default value of "255"
    """
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


# EVENT_SET_VALUE
def setValue(variable = "L0", value = "0"):
    """
    Generated method for the GBS script action EVENT_SET_VALUE.

    variable: str with a default value of "L0"
    value: str with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_SET_VALUE"
    element["args"] = {
        "variable": variable,
        "value": value,
    }
    return element


# EVENT_SET_RANDOM_VALUE
def setRandomValue():
    """
    Generated method for the GBS script action EVENT_SET_RANDOM_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_SET_RANDOM_VALUE"
    return element


# EVENT_INC_VALUE
def incValue(variable = "L0"):
    """
    Generated method for the GBS script action EVENT_INC_VALUE.

    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_INC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element


# EVENT_DEC_VALUE
def decValue(variable = "L0"):
    """
    Generated method for the GBS script action EVENT_DEC_VALUE.

    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_DEC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element


# EVENT_MATH_ADD
def mathAdd():
    """
    Generated method for the GBS script action EVENT_MATH_ADD.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_ADD"
    return element


# EVENT_MATH_SUB
def mathSub():
    """
    Generated method for the GBS script action EVENT_MATH_SUB.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_SUB"
    return element


# EVENT_MATH_MUL
def mathMul():
    """
    Generated method for the GBS script action EVENT_MATH_MUL.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_MUL"
    return element


# EVENT_MATH_DIV
def mathDiv():
    """
    Generated method for the GBS script action EVENT_MATH_DIV.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_DIV"
    return element


# EVENT_MATH_MOD
def mathMod():
    """
    Generated method for the GBS script action EVENT_MATH_MOD.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_MOD"
    return element


# EVENT_MATH_ADD_VALUE
def mathAddValue():
    """
    Generated method for the GBS script action EVENT_MATH_ADD_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_ADD_VALUE"
    return element


# EVENT_MATH_SUB_VALUE
def mathSubValue():
    """
    Generated method for the GBS script action EVENT_MATH_SUB_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_SUB_VALUE"
    return element


# EVENT_MATH_MUL_VALUE
def mathMulValue():
    """
    Generated method for the GBS script action EVENT_MATH_MUL_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_MUL_VALUE"
    return element


# EVENT_MATH_DIV_VALUE
def mathDivValue():
    """
    Generated method for the GBS script action EVENT_MATH_DIV_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_DIV_VALUE"
    return element


# EVENT_MATH_MOD_VALUE
def mathModValue():
    """
    Generated method for the GBS script action EVENT_MATH_MOD_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_MATH_MOD_VALUE"
    return element


# EVENT_COPY_VALUE
def copyValue():
    """
    Generated method for the GBS script action EVENT_COPY_VALUE.

    """
    element = makeElement()
    element["command"] = "EVENT_COPY_VALUE"
    return element


# EVENT_SET_FLAGS
def setFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    """
    Generated method for the GBS script action EVENT_SET_FLAGS.

    variable: str with a default value of "L0"
    flag1: bool with a default value of "False"
    flag2: bool with a default value of "False"
    flag3: bool with a default value of "False"
    flag4: bool with a default value of "False"
    flag5: bool with a default value of "False"
    flag6: bool with a default value of "False"
    flag7: bool with a default value of "False"
    flag8: bool with a default value of "False"
    """
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


# EVENT_ADD_FLAGS
def addFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    """
    Generated method for the GBS script action EVENT_ADD_FLAGS.

    variable: str with a default value of "L0"
    flag1: bool with a default value of "False"
    flag2: bool with a default value of "False"
    flag3: bool with a default value of "False"
    flag4: bool with a default value of "False"
    flag5: bool with a default value of "False"
    flag6: bool with a default value of "False"
    flag7: bool with a default value of "False"
    flag8: bool with a default value of "False"
    """
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


# EVENT_CLEAR_FLAGS
def clearFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    """
    Generated method for the GBS script action EVENT_CLEAR_FLAGS.

    variable: str with a default value of "L0"
    flag1: bool with a default value of "False"
    flag2: bool with a default value of "False"
    flag3: bool with a default value of "False"
    flag4: bool with a default value of "False"
    flag5: bool with a default value of "False"
    flag6: bool with a default value of "False"
    flag7: bool with a default value of "False"
    flag8: bool with a default value of "False"
    """
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


# EVENT_IF_FLAGS_COMPARE
def ifFlagsCompare(variable = "L0", flag = "1", __collapseElse = "False", children = {'true': [], 'false': []}):
    """
    Generated method for the GBS script action EVENT_IF_FLAGS_COMPARE.

    variable: str with a default value of "L0"
    flag: int with a default value of "1"
    __collapseElse: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_IF_FLAGS_COMPARE"
    element["args"] = {
        "variable": variable,
        "flag": flag,
        "__collapseElse": __collapseElse,
    }

    element["children"] = {}
    for cmd_key, cmd_list in children.items():
        #cmd_list.append(end())
        element["children"][cmd_key] = cmd_list
    return element


# EVENT_AWAIT_INPUT
def awaitInput(input = "['a', 'b']"):
    """
    Generated method for the GBS script action EVENT_AWAIT_INPUT.

    input: list with a default value of "['a', 'b']"
    """
    element = makeElement()
    element["command"] = "EVENT_AWAIT_INPUT"
    element["args"] = {
        "input": input,
    }
    return element


# EVENT_TEXT
def text(text = "'push", avatarId = ""):
    """
    Generated method for the GBS script action EVENT_TEXT.

    text: str with a default value of "'push"
    avatarId: str with a default value of ""
    """
    element = makeElement()
    element["command"] = "EVENT_TEXT"
    element["args"] = {
        "text": text,
        "avatarId": avatarId,
    }
    return element


# EVENT_TEXT_SET_ANIMATION_SPEED
def textSetAnimationSpeed(speedIn = "1", speedOut = "1", speed = "1"):
    """
    Generated method for the GBS script action EVENT_TEXT_SET_ANIMATION_SPEED.

    speedIn: int with a default value of "1"
    speedOut: int with a default value of "1"
    speed: int with a default value of "1"
    """
    element = makeElement()
    element["command"] = "EVENT_TEXT_SET_ANIMATION_SPEED"
    element["args"] = {
        "speedIn": speedIn,
        "speedOut": speedOut,
        "speed": speed,
    }
    return element


# EVENT_ACTOR_SET_DIRECTION
def actorSetDirection(actorId = "player", direction = "up"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_DIRECTION.

    actorId: str with a default value of "player"
    direction: str with a default value of "up"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element


# EVENT_ACTOR_SET_DIRECTION_TO_VALUE
def actorSetDirectionToValue(actorId = "player", variable = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_DIRECTION_TO_VALUE.

    actorId: str with a default value of "player"
    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_DIRECTION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element


# EVENT_ACTOR_SET_POSITION
def actorSetPosition(actorId = "player", x = "0", y = "0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_POSITION.

    actorId: str with a default value of "player"
    x: int with a default value of "0"
    y: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element


# EVENT_ACTOR_SET_POSITION_RELATIVE
def actorSetPositionRelative(actorId = "player", x = "0", y = "0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_POSITION_RELATIVE.

    actorId: str with a default value of "player"
    x: int with a default value of "0"
    y: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element


# EVENT_ACTOR_MOVE_RELATIVE
def actorMoveRelative(actorId = "player", x = "0", y = "0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_MOVE_RELATIVE.

    actorId: str with a default value of "player"
    x: int with a default value of "0"
    y: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element


# EVENT_ACTOR_MOVE_TO
def actorMoveTo():
    """
    Generated method for the GBS script action EVENT_ACTOR_MOVE_TO.

    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_TO"
    return element


# EVENT_ACTOR_PUSH
def actorPush(do_continue = "False"):
    """
    Generated method for the GBS script action EVENT_ACTOR_PUSH.

    do_continue: bool with a default value of "False"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_PUSH"
    element["args"] = {
        "continue": do_continue,
    }
    return element


# EVENT_ACTOR_SET_ANIMATION_SPEED
def actorSetAnimationSpeed(actorId = "player", speed = "3"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_ANIMATION_SPEED.

    actorId: str with a default value of "player"
    speed: str with a default value of "3"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_ANIMATION_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element


# EVENT_ACTOR_SET_MOVEMENT_SPEED
def actorSetMovementSpeed(actorId = "player", speed = "1"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_MOVEMENT_SPEED.

    actorId: str with a default value of "player"
    speed: str with a default value of "1"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_MOVEMENT_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element


# EVENT_ACTOR_EMOTE
def actorEmote(actorId = "player", emoteId = "0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_EMOTE.

    actorId: str with a default value of "player"
    emoteId: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_EMOTE"
    element["args"] = {
        "actorId": actorId,
        "emoteId": emoteId,
    }
    return element


# EVENT_PLAYER_SET_SPRITE
def playerSetSprite(spriteSheetId = "468ef314-e09e-42e2-8778-99e1331e8beb"):
    """
    Generated method for the GBS script action EVENT_PLAYER_SET_SPRITE.

    spriteSheetId: str with a default value of "468ef314-e09e-42e2-8778-99e1331e8beb"
    """
    element = makeElement()
    element["command"] = "EVENT_PLAYER_SET_SPRITE"
    element["args"] = {
        "spriteSheetId": spriteSheetId,
    }
    return element


# EVENT_ACTOR_GET_POSITION
def actorGetPosition(actorId = "player", vectorX = "L0", vectorY = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_GET_POSITION.

    actorId: str with a default value of "player"
    vectorX: str with a default value of "L0"
    vectorY: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_GET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element


# EVENT_ACTOR_GET_DIRECTION
def actorGetDirection(actorId = "player", direction = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_GET_DIRECTION.

    actorId: str with a default value of "player"
    direction: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_GET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element


# EVENT_ACTOR_SET_POSITION_TO_VALUE
def actorSetPositionToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_POSITION_TO_VALUE.

    actorId: str with a default value of "player"
    vectorX: str with a default value of "L0"
    vectorY: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_POSITION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element


# EVENT_ACTOR_MOVE_TO_VALUE
def actorMoveToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_MOVE_TO_VALUE.

    actorId: str with a default value of "player"
    vectorX: str with a default value of "L0"
    vectorY: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_MOVE_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element


# EVENT_ACTOR_INVOKE
def actorInvoke(actorId = "82444b20-65df-436a-b1c1-191aacf2258d"):
    """
    Generated method for the GBS script action EVENT_ACTOR_INVOKE.

    actorId: str with a default value of "82444b20-65df-436a-b1c1-191aacf2258d"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_INVOKE"
    element["args"] = {
        "actorId": actorId,
    }
    return element


# EVENT_ACTOR_SET_FRAME
def actorSetFrame(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", frame = "0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_FRAME.

    actorId: str with a default value of "82444b20-65df-436a-b1c1-191aacf2258d"
    frame: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_FRAME"
    element["args"] = {
        "actorId": actorId,
        "frame": frame,
    }
    return element


# EVENT_ACTOR_SET_FRAME_TO_VALUE
def actorSetFrameToValue(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", variable = "L0"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SET_FRAME_TO_VALUE.

    actorId: str with a default value of "82444b20-65df-436a-b1c1-191aacf2258d"
    variable: str with a default value of "L0"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SET_FRAME_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element


# EVENT_CAMERA_MOVE_TO
def cameraMoveTo(x = "0", y = "0", speed = "0"):
    """
    Generated method for the GBS script action EVENT_CAMERA_MOVE_TO.

    x: int with a default value of "0"
    y: int with a default value of "0"
    speed: str with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_CAMERA_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element


# EVENT_CAMERA_LOCK
def cameraLock(speed = "0"):
    """
    Generated method for the GBS script action EVENT_CAMERA_LOCK.

    speed: str with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_CAMERA_LOCK"
    element["args"] = {
        "speed": speed,
    }
    return element


# EVENT_CAMERA_SHAKE
def cameraShake(time = "0.5"):
    """
    Generated method for the GBS script action EVENT_CAMERA_SHAKE.

    time: float with a default value of "0.5"
    """
    element = makeElement()
    element["command"] = "EVENT_CAMERA_SHAKE"
    element["args"] = {
        "time": time,
    }
    return element


# EVENT_FADE_OUT
def fadeOut(speed = "2"):
    """
    Generated method for the GBS script action EVENT_FADE_OUT.

    speed: str with a default value of "2"
    """
    element = makeElement()
    element["command"] = "EVENT_FADE_OUT"
    element["args"] = {
        "speed": speed,
    }
    return element


# EVENT_FADE_IN
def fadeIn(speed = "2"):
    """
    Generated method for the GBS script action EVENT_FADE_IN.

    speed: str with a default value of "2"
    """
    element = makeElement()
    element["command"] = "EVENT_FADE_IN"
    element["args"] = {
        "speed": speed,
    }
    return element


# EVENT_SHOW_SPRITES
def showSprites():
    """
    Generated method for the GBS script action EVENT_SHOW_SPRITES.

    """
    element = makeElement()
    element["command"] = "EVENT_SHOW_SPRITES"
    return element


# EVENT_HIDE_SPRITES
def hideSprites():
    """
    Generated method for the GBS script action EVENT_HIDE_SPRITES.

    """
    element = makeElement()
    element["command"] = "EVENT_HIDE_SPRITES"
    return element


# EVENT_ACTOR_SHOW
def actorShow(actorId = "player"):
    """
    Generated method for the GBS script action EVENT_ACTOR_SHOW.

    actorId: str with a default value of "player"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_SHOW"
    element["args"] = {
        "actorId": actorId,
    }
    return element


# EVENT_ACTOR_HIDE
def actorHide(actorId = "player"):
    """
    Generated method for the GBS script action EVENT_ACTOR_HIDE.

    actorId: str with a default value of "player"
    """
    element = makeElement()
    element["command"] = "EVENT_ACTOR_HIDE"
    element["args"] = {
        "actorId": actorId,
    }
    return element


# EVENT_OVERLAY_SHOW
def overlayShow(color = "black", x = "0", y = "0"):
    """
    Generated method for the GBS script action EVENT_OVERLAY_SHOW.

    color: str with a default value of "black"
    x: int with a default value of "0"
    y: int with a default value of "0"
    """
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_SHOW"
    element["args"] = {
        "color": color,
        "x": x,
        "y": y,
    }
    return element


# EVENT_OVERLAY_HIDE
def overlayHide():
    """
    Generated method for the GBS script action EVENT_OVERLAY_HIDE.

    """
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_HIDE"
    return element


# EVENT_OVERLAY_MOVE_TO
def overlayMoveTo(x = "0", y = "0", speed = "1"):
    """
    Generated method for the GBS script action EVENT_OVERLAY_MOVE_TO.

    x: int with a default value of "0"
    y: int with a default value of "0"
    speed: str with a default value of "1"
    """
    element = makeElement()
    element["command"] = "EVENT_OVERLAY_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element


# EVENT_MUSIC_PLAY
def musicPlay(musicId = "56622189-8327-4a64-bd29-2fbcf243c97e", loop = "True"):
    """
    Generated method for the GBS script action EVENT_MUSIC_PLAY.

    musicId: str with a default value of "56622189-8327-4a64-bd29-2fbcf243c97e"
    loop: bool with a default value of "True"
    """
    element = makeElement()
    element["command"] = "EVENT_MUSIC_PLAY"
    element["args"] = {
        "musicId": musicId,
        "loop": loop,
    }
    return element


# EVENT_MUSIC_STOP
def musicStop():
    """
    Generated method for the GBS script action EVENT_MUSIC_STOP.

    """
    element = makeElement()
    element["command"] = "EVENT_MUSIC_STOP"
    return element


# EVENT_SOUND_PLAY_BEEP
def soundPlayBeep():
    """
    Generated method for the GBS script action EVENT_SOUND_PLAY_BEEP.

    """
    element = makeElement()
    element["command"] = "EVENT_SOUND_PLAY_BEEP"
    return element


# EVENT_CALL_CUSTOM_EVENT
def callCustomEvent(customEventId = "4bf11658-2bb2-4e79-ad96-22577c9a8353", __name = "Custom Event 1"):
    """
    Generated method for the GBS script action EVENT_CALL_CUSTOM_EVENT.

    customEventId: str with a default value of "4bf11658-2bb2-4e79-ad96-22577c9a8353"
    __name: str with a default value of "Custom Event 1"
    """
    element = makeElement()
    element["command"] = "EVENT_CALL_CUSTOM_EVENT"
    element["args"] = {
        "customEventId": customEventId,
        "__name": __name,
    }
    return element
