### Script Commands ###
script_commands = {
    "EVENT_END": {},  # no arguments
    "EVENT_STOP": {},  # no arguments, same as end
    "EVENT_WAIT": {
        "time": 0.5
    },
    # Scenes
    "EVENT_SWITCH_SCENE": {
        "sceneId": "498cfdcf-3000-453f-9b52-fe5d8d81cac2",
        "x": 7,
        "y": 6,
        "direction": "",
        "fadeSpeed": "2"
    },
    "EVENT_START_BATTLE": {},
    "EVENT_RETURN_TO_TITLE": {},
    "EVENT_SCENE_PUSH_STATE": {None:None},  # needs empty args????
    "EVENT_SCENE_POP_STATE": {
        "fadeSpeed": "2"
    },
    "EVENT_SCENE_RESET_STATE": {},  # no arguments
    "EVENT_SCENE_POP_ALL_STATE": {
        "fadeSpeed": "2"
    },
    # Data
    "EVENT_LOAD_DATA": {None:None},  # needs empty args????????
    "EVENT_SAVE_DATA": {},  # no arguments
    "EVENT_CLEAR_DATA": {},  # no arguments
    # Conditional
    "EVENT_IF_TRUE": {
        "variable": "L0",
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_FALSE": {
        "variable": "L0",
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_VALUE": {
        "variable": "L3",
        "operator": ">",
        "comparator": 2,
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_VALUE_COMPARE": {
        "vectorX": "6",
        "operator": "==",
        "vectorY": "3",
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_INPUT": {
        "input": [
            "a",
            "b"
        ],
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_ACTOR_DIRECTION": {
        "actorId": "player",
        "direction": "up",
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_SAVED_DATA": {
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_IF_ACTOR_AT_POSITION": {
        "actorId": "player",
        "x": 0,
        "y": 0,
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    "EVENT_SET_TRUE": {
        "variable": "L0"
    },
    "EVENT_SET_FALSE": {
        "variable": "L0"
    },
    "EVENT_CHOICE": {
        "variable": "L0",
        "trueText": "",
        "falseText": ""
    },
    "EVENT_RESET_VARIABLES": {},  # no arguments
    "EVENT_LOOP": {"children": ["true"]},  # no arguments
    "EVENT_GROUP": {"children": ["true"]},  # no arguments
    "EVENT_MENU": {
        "variable": "L0",
        "items": 2,
        "option1": "",
        "option2": "",
        "option3": "",
        "option4": "",
        "option5": "",
        "option6": "",
        "option7": "",
        "option8": "",
        "cancelOnB": True,
        "layout": "dialogue"
    },
    "EVENT_COMMENT": {
        "text": ""
    },
    # Background Scripts
    "EVENT_SET_INPUT_SCRIPT": {
        "input": "b",
        "children": ["true"]
    },
    "EVENT_SET_BACKGROUND_SCRIPT": {},
    "EVENT_REMOVE_INPUT_SCRIPT": {  # look into more, is the remove imput scrip
        "input": [
            "b"
        ]
    },
    # Math
    "EVENT_VARIABLE_MATH": {
        "vectorX": "L0",
        "operation": "set",
        "other": "true",
        "vectorY": "L0",
        "value": "1",
        "minValue": "0",
        "maxValue": "255"
    },
    "EVENT_SET_VALUE": {
        "variable": "L0",
        "value": "0"
    },
    "EVENT_SET_RANDOM_VALUE": {},
    "EVENT_INC_VALUE": {
        "variable": "L0"
    },
    "EVENT_DEC_VALUE": {
        "variable": "L0"
    },
    "EVENT_MATH_ADD": {},
    "EVENT_MATH_SUB": {},
    "EVENT_MATH_MUL": {},
    "EVENT_MATH_DIV": {},
    "EVENT_MATH_MOD": {},
    "EVENT_MATH_ADD_VALUE": {},
    "EVENT_MATH_SUB_VALUE": {},
    "EVENT_MATH_MUL_VALUE": {},
    "EVENT_MATH_DIV_VALUE": {},
    "EVENT_MATH_MOD_VALUE": {},
    "EVENT_COPY_VALUE": {},
    "EVENT_SET_FLAGS": {
        "variable": "L0",
        "flag1": False,
        "flag2": False,
        "flag3": False,
        "flag4": False,
        "flag5": False,
        "flag6": False,
        "flag7": False,
        "flag8": False
    },
    "EVENT_ADD_FLAGS": {
        "variable": "L0",
        "flag1": False,
        "flag2": False,
        "flag3": False,
        "flag4": False,
        "flag5": False,
        "flag6": False,
        "flag7": False,
        "flag8": False
    },
    "EVENT_CLEAR_FLAGS": {
        "variable": "L0",
        "flag1": False,
        "flag2": False,
        "flag3": False,
        "flag4": False,
        "flag5": False,
        "flag6": False,
        "flag7": False,
        "flag8": False
    },
    "EVENT_IF_FLAGS_COMPARE": {
        "variable": "L0",
        "flag": 1,
        "__collapseElse": False,
        "children": ["true", "false"]
    },
    # Input
    "EVENT_AWAIT_INPUT": {
        "input": [
            "a",
            "b"
        ]
    },
    # Actor
    "EVENT_TEXT": {
        "text": "'push",
        "avatarId": ""
    },
    "EVENT_TEXT_SET_ANIMATION_SPEED": {
        "speedIn": 1,
        "speedOut": 1,
        "speed": 1
    },
    "EVENT_ACTOR_SET_DIRECTION": {
        "actorId": "player",
        "direction": "up"
    },
    "EVENT_ACTOR_SET_DIRECTION_TO_VALUE": {
        "actorId": "player",
        "variable": "L0"
    },
    "EVENT_ACTOR_SET_POSITION": {
        "actorId": "player",
        "x": 0,
        "y": 0
    },
    "EVENT_ACTOR_SET_POSITION_RELATIVE": {
        "actorId": "player",
        "x": 0,
        "y": 0},
    "EVENT_ACTOR_MOVE_RELATIVE": {
        "actorId": "player",
        "x": 0,
        "y": 0
    },
    "EVENT_ACTOR_MOVE_TO": {},
    "EVENT_ACTOR_PUSH": {
        "continue": False
    },
    "EVENT_ACTOR_SET_ANIMATION_SPEED": {
        "actorId": "player",
        "speed": "3"
    },
    "EVENT_ACTOR_SET_MOVEMENT_SPEED": {
        "actorId": "player",
        "speed": "1"
    },
    "EVENT_ACTOR_EMOTE": {
        "actorId": "player",
        "emoteId": 0
    },
    "EVENT_PLAYER_SET_SPRITE": {
        "spriteSheetId": "468ef314-e09e-42e2-8778-99e1331e8beb"
    },
    "EVENT_ACTOR_GET_POSITION": {
        "actorId": "player",
        "vectorX": "L0",
        "vectorY": "L0"
    },
    "EVENT_ACTOR_GET_DIRECTION": {
        "actorId": "player",
        "direction": "L0"
    },
    "EVENT_ACTOR_SET_POSITION_TO_VALUE": {
        "actorId": "player",
        "vectorX": "L0",
        "vectorY": "L0"
    },
    "EVENT_ACTOR_MOVE_TO_VALUE": {
        "actorId": "player",
        "vectorX": "L0",
        "vectorY": "L0"
    },
    "EVENT_ACTOR_INVOKE": {
        "actorId": "82444b20-65df-436a-b1c1-191aacf2258d"
    },
    "EVENT_ACTOR_SET_FRAME": {
        "actorId": "82444b20-65df-436a-b1c1-191aacf2258d",
        "frame": 0
    },
    "EVENT_ACTOR_SET_FRAME_TO_VALUE": {
        "actorId": "82444b20-65df-436a-b1c1-191aacf2258d",
        "variable": "L0"
    },
    # Camera
    "EVENT_CAMERA_MOVE_TO": {
        "x": 0,
        "y": 0,
        "speed": "0"
    },
    "EVENT_CAMERA_LOCK": {
        "speed": "0"
    },
    "EVENT_CAMERA_SHAKE": {
        "time": 0.5
    },
    "EVENT_FADE_OUT": {
        "speed": "2"
    },
    "EVENT_FADE_IN": {
        "speed": "2"
    },
    "EVENT_SHOW_SPRITES": {},  # no arguments
    "EVENT_HIDE_SPRITES": {},  # no arguments
    "EVENT_ACTOR_SHOW": {
        "actorId": "player"
    },
    "EVENT_ACTOR_HIDE": {
        "actorId": "player"
    },
    # Overlay
    "EVENT_OVERLAY_SHOW": {
        "color": "black",
        "x": 0,
        "y": 0
    },
    "EVENT_OVERLAY_HIDE": {},  # no arguments
    "EVENT_OVERLAY_MOVE_TO": {"x": 0, "y": 0, "speed": "1"},
    # Music
    "EVENT_MUSIC_PLAY": {
        "musicId": "56622189-8327-4a64-bd29-2fbcf243c97e",
        "loop": True
    },
    "EVENT_MUSIC_STOP": {},  # no arguments
    # Sound
    "EVENT_SOUND_PLAY_BEEP": {},
    # Call CustomEvent
    "EVENT_CALL_CUSTOM_EVENT": {
        "customEventId": "4bf11658-2bb2-4e79-ad96-22577c9a8353",
        "__name": "Custom Event 1"
    }
}


def getScript():
    return script_commands
