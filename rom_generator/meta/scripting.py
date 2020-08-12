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
        },
    'EVENT_ACTOR_SET_ACTIVE': {
        # unknown
    },
    'EVENT_ACTOR_SET_ANIM_SPEED': {
        "actorId": "player",
        "speed": 3
    },
    'EVENT_ACTOR_SET_FLIP': {
        # unknown
    },
    'EVENT_ACTOR_SET_MOVE_SPEED': {
        "actorId": "player",
        "speed": 1
    },
    'EVENT_JUMP': {
        #unknown
    },
    'EVENT_LOAD_VECTORS': {
        #unknown
    },
	'EVENT_NEXT_FRAME': {
        #unknown
    },
	'EVENT_NOOP': {}, # Unknown, probably no fields
	'EVENT_OVERLAY_SET_POSITION': {}, # Unknown
    'EVENT_SCENE_RESET_STATE': {}, # No fields
	'EVENT_SCENE_STATE_RESET': {}, # ???
	'EVENT_SET_TIMER_SCRIPT': {
        "duration": 10.0,
        "script": [],
        "children": {}
    },
	'EVENT_SOUND_PLAY_CRASH': {}, # Unknown
	'EVENT_SOUND_START_TONE': {}, # Unknown
	'EVENT_SOUND_STOP_TONE': {}, # Unknown
	'EVENT_STACK_POP': {}, # Unknown
	'EVENT_STACK_PUSH': {}, # Unknown
	'EVENT_TEXT_MULTI': {}, # Unknown
	'EVENT_TEXT_SET_ANIM_SPEED': {
        "speedIn": 1,
        "speedOut": 1,
        "cameraSpeed": 1
    },
	'EVENT_TEXT_WITH_AVATAR': {
        "text": "",
        "avatarId": ""
    },
	'EVENT_TIMER_DISABLE': {}, # No fields
	'EVENT_TIMER_RESTART': {}, # No fields
	'EVENT_VARIABLE_ADD_FLAGS': {
    "variable": "LAST_VARIABLE",
  	"flag1": False,
  	"flag2": False,
    "flag3": False,
  	"flag4": False,
  	"flag5": False,
  	"flag6": False,
  	"flag7": False,
  	"flag8": False
    },
	'EVENT_VARIABLE_CLEAR_FLAGS': {
        "variable": "LAST_VARIABLE",
      	"flag1": False,
      	"flag2": False,
        "flag3": False,
      	"flag4": False,
      	"flag5": False,
      	"flag6": False,
      	"flag7": False,
      	"flag8": False
    },
    "EVENT_SWITCH": {
        "variable": "LAST_VARIABLE",
        "choices": 2,
        "value0": 1,
        "value1": 2,
        "value2": 3,
        "value3": 4,
        "value4": 5,
        "value5": 6,
        "value6": 7,
        "value7": 8,
        "value8": 9,
        "value9": 10,
        "value10": 11,
        "value11": 12,
        "value12": 13,
        "value13": 14,
        "value14": 15,
        "value15": 16,
        "children": {"true0": [], "true1": [], "true2": [], "true3": [], "true4": [], "true5": [], "true6": [], "true7": [], "true8": [], "true9": [], "true10": [], "true11": [], "true12": [], "true13": [], "true14": [], "true15": [], "true16": []}

    }
}

# List of script commands from GBS
GBSscriptCommands = [
  "END", "TEXT", "JUMP", "IF_TRUE", "NOOP", "SET_TRUE", "SET_FALSE", "ACTOR_SET_DIRECTION", "ACTOR_SET_ACTIVE", "CAMERA_MOVE_TO", "CAMERA_LOCK", "WAIT", "FADE_OUT", "FADE_IN", "SWITCH_SCENE", "ACTOR_SET_POSITION", "ACTOR_MOVE_TO", "SHOW_SPRITES", "HIDE_SPRITES", "PLAYER_SET_SPRITE", "ACTOR_SHOW", "ACTOR_HIDE", "ACTOR_EMOTE", "CAMERA_SHAKE", "RETURN_TO_TITLE", "OVERLAY_SHOW", "OVERLAY_HIDE", "OVERLAY_SET_POSITION", "OVERLAY_MOVE_TO", "AWAIT_INPUT", "MUSIC_PLAY", "MUSIC_STOP", "RESET_VARIABLES", "NEXT_FRAME", "INC_VALUE", "DEC_VALUE", "SET_VALUE", "IF_VALUE", "IF_INPUT", "CHOICE", "ACTOR_PUSH", "IF_ACTOR_AT_POSITION", "LOAD_DATA", "SAVE_DATA", "CLEAR_DATA", "IF_SAVED_DATA", "IF_ACTOR_DIRECTION", "SET_RANDOM_VALUE", "ACTOR_GET_POSITION", "ACTOR_SET_POSITION_TO_VALUE", "ACTOR_MOVE_TO_VALUE", "ACTOR_MOVE_RELATIVE", "ACTOR_SET_POSITION_RELATIVE", "MATH_ADD", "MATH_SUB", "MATH_MUL", "MATH_DIV", "MATH_MOD", "MATH_ADD_VALUE", "MATH_SUB_VALUE", "MATH_MUL_VALUE", "MATH_DIV_VALUE", "MATH_MOD_VALUE", "COPY_VALUE", "IF_VALUE_COMPARE", "LOAD_VECTORS", "ACTOR_SET_MOVE_SPEED", "ACTOR_SET_ANIM_SPEED", "TEXT_SET_ANIM_SPEED", "SCENE_PUSH_STATE", "SCENE_POP_STATE", "ACTOR_INVOKE", "STACK_PUSH", "STACK_POP", "SCENE_STATE_RESET", "SCENE_POP_ALL_STATE", "SET_INPUT_SCRIPT", "REMOVE_INPUT_SCRIPT", "ACTOR_SET_FRAME", "ACTOR_SET_FLIP", "TEXT_MULTI", "ACTOR_SET_FRAME_TO_VALUE", "VARIABLE_ADD_FLAGS", "VARIABLE_CLEAR_FLAGS", "SOUND_START_TONE", "SOUND_STOP_TONE", "SOUND_PLAY_BEEP", "SOUND_PLAY_CRASH", "SET_TIMER_SCRIPT", "TIMER_RESTART", "TIMER_DISABLE", "TEXT_WITH_AVATAR", "MENU"
];


def getScript():
    return script_commands

if __name__ == '__main__':
    import pprint
    e_names = ["_".join(x.split("_")[1:]) for x in getScript().keys()]
    #pprint.pprint(set(e_names))
    print("Missing Commands:")
    pprint.pprint(set(GBSscriptCommands) - set(e_names))
    #pprint.pprint(set(getScript().keys()))
