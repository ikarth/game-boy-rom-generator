import uuid
import copy

### Create a basic GBS element, with a unique ID
def makeElement():
    element = {}
    element["id"] = str(uuid.uuid4())
    return copy.deepcopy(element)

# Translate GBStudio script commands to our function names...
def translateScriptCommandNames(i):
    n = "def " + i[6].lower()
    for j in range(7, len(i)):
        if(i[j] != '_'):
            if(i[j - 1] == '_'):
                n+=i[j]
            else:
                n += i[j].lower()
    return n


## Just some colors for fancy printing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
