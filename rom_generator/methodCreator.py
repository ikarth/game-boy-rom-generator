from scripting import getScript

''' Current issues in this generator

-If given argument is a keyword, generator does not detect this (actorPush())
-If the method has children(specified in the gbsproj file) but does not have __collapseElse, the method will
    need to be manually updated 
    ie() EventLoop(), EventGroup(), EventSetInputScript(), EventCallCustomEvent()

REPLACE THIS TO LOOP
def loop(loopCommand):
    element = makeElement()
    element["commands"] = "EVENT_LOOP"
    element["args"] = {
    }
    loopCommand.add(end())
    element["children"] = {
        "true": loopCommand
    }
    return element

REPLACE THIS TO GROUP
def group(groupCommands):
    element = makeElement()
    element["commands"] = "EVENT_GROUP"
    element["args"] = {
    }
    groupCommands.add(end())
    element["children"] = {
        "true": groupCommands
    }
    return element

REPLACE THIS TO SETINPUTSCRIPT
def setInputScript(input = "b",scripts=[]):
    element = makeElement()
    element["commands"] = "EVENT_SET_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    scripts.add(end())
    element["children"] = {
        "true": scripts
    }
    return element

I DON'T UNDERSTAND CALL CUSTOM EVENTS SO YOURE GOING TO HAVE TO 
    DO THIS YOURSELF
'''

scriptCommands = getScript()
methods = list(scriptCommands.keys())
spacing = "    "
for i in methods:
    n = "def " + i[6].lower()
    for j in range(7, len(i)):
        if(i[j] != '_'):
            if(i[j - 1] == '_'):
                n+=i[j]
            else:
                n += i[j].lower()
    n += "("
    f = False
    l = list(scriptCommands[i].keys())
    for k in l:
        if str(k) == "__collapseElse":
            f = True
        n+= k + " = \"" + str(scriptCommands[i][k]) + "\", "
    
    if f:
       n += "trueCommands = [], falseCommands = []" 
    elif len(l) > 0:
        n = n[0:len(n) - 2]
    n += "):"
    print(n)
    n = spacing + "element = makeElement()"
    print(n)
    n = spacing + "element[\"commands\"] = \"" + i + "\""
    print(n)
    n = spacing + "element[\"args\"] = {"
    print(n)
    for k in l:
        n = spacing + spacing + "\"" + k + "\": " + k + ","
        print(n)
    print(spacing + "}")

    if f:
        n = spacing + "trueCommands.add(end())"
        print(n)
        n = spacing + "falseCommands.add(end())"
        print(n)
        n = spacing + "element[\"children\"] = {"
        print(n)
        n = spacing + spacing + "\"true\": trueCommands,"
        print(n)
        n = spacing + spacing + "\"false\": falseCommands"
        print(n)
        print(spacing + "}")
    print(spacing + "return element")
    print()
