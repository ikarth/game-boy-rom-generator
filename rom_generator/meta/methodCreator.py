import keyword
from .scripting import getScript

''' Current issues in this generator

-If given argument is a keyword, generator does not detect this (actorPush())
-If the method has children(specified in the gbsproj file) but does not have __collapseElse, the method will
    need to be manually updated
    ie() EventLoop(), EventGroup(), EventSetInputScript(), EventCallCustomEvent()

REPLACE THIS TO LOOP
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

REPLACE THIS TO GROUP
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

REPLACE THIS TO SETINPUTSCRIPT
def setInputScript(input = "b",scripts=[]):
    element = makeElement()
    element["command"] = "EVENT_SET_INPUT_SCRIPT"
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

child_clause = '''
element["children"] = {}
for cmd_key, cmd_list in children.items():
    # cmd_list.append(end())
    element["children"][cmd_key] = cmd_list
'''


def generateScriptMethods():
    emitted_code = "# Generated methods for scripts\nfrom rom_generator.utilities import makeElement\n\n"
    def emit_code(input_str):
        nonlocal emitted_code
        print(input_str)
        emitted_code += input_str + "\n"

    scriptCommands = getScript()
    methods = list(scriptCommands.keys())
    spacing = "    "
    for input_method in methods:
        emit_code(f"\n# {input_method}")
        code_line_string = "def " + input_method[6].lower()
        for j in range(7, len(input_method)):
            if(input_method[j] != '_'):
                if(input_method[j - 1] == '_'):
                    code_line_string += input_method[j]
                else:
                    code_line_string += input_method[j].lower()
        code_line_string += "("
        has_collapse_else_f = False
        has_children = False
        list_of_cmds = list(scriptCommands[input_method].keys())
        argument_list = []
        for k in list_of_cmds:
            if str(k) == "__collapseElse":
                has_collapse_else_f = True
            if str(k) == "children":
                has_children = True
            else:
                k_str = str(k)
                if keyword.iskeyword(k):
                    k_str = "do_" + str(k)
                arg_def = scriptCommands[input_method][k]
                arg_type = str(type(arg_def).__name__)
                argument_list.append(k_str + f": {arg_type} with a default value of \"{str(arg_def)}\"")
                code_line_string += k_str + " = \"" + str(scriptCommands[input_method][k]) + "\", "

        if has_collapse_else_f or has_children:
            code_line_string += "children = {"
            child_entry_strings = [f"\'{child_entry}\': []" for child_entry in scriptCommands[input_method]["children"]]
            code_line_string += ", ".join(child_entry_strings)
            code_line_string += "}"
        elif len(list_of_cmds) > 0:
            code_line_string = code_line_string[0:len(code_line_string) - 2]
        code_line_string += "):"
        emit_code(code_line_string)

        emit_code(spacing + "\"\"\"")
        emit_code(spacing + f"Generated method for the GBS script action {input_method}.\n")
        for arg_item in argument_list:
            emit_code(spacing + arg_item)
        emit_code(spacing + "\"\"\"")

        code_line_string = spacing + "element = makeElement()"
        emit_code(code_line_string)
        code_line_string = spacing + "element[\"command\"] = \"" + input_method + "\""
        emit_code(code_line_string)
        if (len(list_of_cmds) > 0):
            code_line_string = spacing + "element[\"args\"] = {"
            emit_code(code_line_string)
            for k in list_of_cmds:
                if "children" == k:
                    pass
                else:
                    k_str = str(k)
                    if keyword.iskeyword(k):
                        k_str = "do_" + str(k)
                    code_line_string = spacing + spacing + "\"" + str(k) + "\": " + k_str + ","
                    emit_code(code_line_string)
            emit_code(spacing + "}")

        if has_collapse_else_f or has_children:
            child_code_lines = child_clause.splitlines()
            for childcodeline in child_code_lines:
                code_line_string = spacing + childcodeline
                emit_code(code_line_string)
        emit_code(spacing + "return element")
        emit_code("")

    return emitted_code

if __name__ == '__main__':
    import os
    rename_number = 0
    emitted = generateScriptMethods()
    rename_source = "rom_generator\\script_functions.py"
    while rename_number >= 0:
        rename_target = f"rom_generator\\script_functions.{rename_number:07d}"
        try:
            os.rename(rename_source, rename_target)
            rename_number = -1
            break
        except FileExistsError as err:
            if rename_number > 9999999:
                raise err
        rename_number += 1

    with open("rom_generator\\script_functions.py", "w", encoding='utf-8') as py_file:
        py_file.write(emitted)
