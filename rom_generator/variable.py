'''
This keeps track of variable spaces that are already taken so that things don't break down
'''

ar = [False] * 501 #the number of variables

counter = 0


def getOpenVariable():
    global ar, counter
    while(ar[counter]):
        counter = counter + 1
    ar[counter] = True
    #print("counter " + str(counter))
    return counter

def deprecatedVariable(index):
    global ar, counter
    ar[index] = False
    if index < counter:
        counter = index