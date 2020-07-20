index = [[]]
parent = []
n = 1
connections = 0

def fillIndex():
    counter = 1
    for i in n:
        for j in n:
            index[i][j] = counter
            counter = counter + 1

def initializeArrays():
    index = [[0 for x in range(n)] for y in range(h)]
    parent = [0 for x in range(n * n)]
    for i in range(1, n * n):
        parent[i] = i

def find(i):
    if(parent[i] == i):
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(a, b):
    k = find(a)
    e = find(b)
    if k != e:
        parent[k] = parent[e]
        connections = connections + 1