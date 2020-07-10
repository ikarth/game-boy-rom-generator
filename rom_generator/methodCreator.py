from scripting import getScript

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
    l = list(scriptCommands[i].keys())
    for k in l:
        n+= k + " = \"" + str(scriptCommands[i][k]) + "\", "
    if len(l) > 0:
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
    print(spacing + "return element")
