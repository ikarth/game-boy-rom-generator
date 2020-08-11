import random

'''
Here this attempts to run  / Kruskals algorithm in maze generation
'''


class block():
    def __init__(self):
        self.ar = [False, False]


class pair():
    def __init__(self, aa, bb, cc):
        self.a = aa
        self.b = bb
        self.ind = cc


edges = []
parent = []
queue = []
holding = [[]]
xdir = [0, 1]
ydir = [1, 0]
n = 1
connections = 0


def initializeArrays():
    global edges, parent, queue, holding, xdir, ydir, n, connections

    edges = []


    parent = []
    queue = []
    holding = [[]]
    connections = 0
    holding = [[block() for w in range(n)] for z in range(n)]
    for x in range(0, n):
        for y in range(0, n):
            if y < n - 1:
                edges.append(pair(x, y, 0))
                #print("Y is " + str(y))
            if x < n - 1:
                edges.append(pair(x, y, 1))
                #print("X is " + str(x))
            holding[x][y] = block()
    parent = [0] * (n * n)
    for i in range(0, n * n):
        #print("INDEX IS " + str(i))
        parent[i] = i


def find(i):
    global parent
    #print("CUR " + str(i))
    if(parent[i] == i):
        return i
    parent[i] = find(parent[i])
    return parent[i]


def union(a, b):
    global parent, connections
    #print("Finding a")
    k = find(a)
    #print("Finding b")
    e = find(b)
    if k != e:
        parent[k] = parent[e]
        connections = connections + 1
        return True
    return False


def run(num):
    global n
    n = num
 
    initializeArrays()
    global edges, connections, holding
    #print("length is " + str(len(edges)))
    #print("length is " + str(len(holding)))
    #print("n is " + str(n))
    random.seed()
    random.shuffle(edges)  # randomize edges
    #print("length is " + str(len(edges)))
    #print(connections < (n * n))
    #print(len(edges) > 0)
    #print(connections < (n * n) and len(edges) > 0)

    while connections != (n * n - 1) and len(edges) > 0:
        index = random.randint(0, len(edges) - 1)
        temp = edges.pop(index)
        #print(temp.b * n + temp.a)

        if(union(temp.b * n + temp.a, (temp.b + ydir[temp.ind]) * n + temp.a + xdir[temp.ind])):
            holding[temp.a][temp.b].ar[temp.ind] = True
            #print("IT WORRRRRKRKRKKRKSRKRSKRSKSR")
        #print("EDgES " + str(len(edges)))
    #print("Connections " + str(connections))
    holding[n - 1][n-1].ar[0] = True


def getList():
    global holding
    return holding


if __name__ == '__main__':
    n = 10
    initializeArrays()
    random.shuffle(parent)
    print(parent)
