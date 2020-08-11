

maps = {}
background = {}
connectionIn = {}
connectionOut = {}

def addSpriteSheet(name = "", spriteSheet = {}):
    '''Adds the sprite Sheet to the project with name name'''
    global maps
    maps[name] = spriteSheet

def findSpriteSheet(name = ""):
    '''Find the sprite sheet wiht the name name'''
    global maps
    return maps[name]

def addBackgroundSpriteSheet(name = "", backgroundSheet = {}):
    '''Adds a background sheet to project with name'''
    global background
    background[name] = backgroundSheet

def findBackgroundSpriteSheet(name = ""):
    '''finds the background spritesheet with name'''
    global background
    return background[name]

def submitBackgroundSpriteSheets(project):
    '''Appends the backgrounds to the spriteSheets'''
    for i, j in background.items():
        project.backgrounds.append(j)

def addInConnections(name = "", connection = []):
    '''Adds in connection to scene of name'''
    global connectionIn
    if name in connectionIn:
        connectionIn[name].append(connection)
    else:
        connectionIn[name] = connection

def findInConnections(name = ""):
    '''Finds the in connection of scene name'''
    global connectionIn
    return connectionIn[name]

def addOutConnections(name = "", connection = []):
    '''Adds the out connection from the scene name'''
    global connectionOut
    if name in connectionOut:
        connectionOut[name].append(connection)
    else:
        connectionOut[name] = connection

def findOutConnection(name = ""):
    '''Finds the out connection of scene name'''
    global connectionOut
    return connectionOut[name]