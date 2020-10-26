#global variables
adjDict = {}
visited = []
path = list()
stack = []
count = 0
scc = {}

def initializeDict(num):
    global adjDict
    global visited
    for i in range(num):
        adjDict[i] = list()
    visited = [False] * num

def addEdge(src, dest):
    global adjDict
    print (f'Adding an edge from {src} to {dest}')
    adjDict[src].append(dest)

def DFSUpdateStack(vertex):
    global adjDict
    global path
    global visited
    global stack

    path.append(vertex)
    visited[vertex] = True

    #If it has neighbours then traverse deep and update stack
    neighbours = adjDict[vertex]
    for ele in neighbours:
        if not visited[ele]:
            DFSUpdateStack(ele)
            stack.append(ele)

def reverseAdjList(c):
    global adjDict
    newAdjDict = adjDict.copy()
    initializeDict(c)

    keys = newAdjDict.keys()
    for src in keys:
        neighbours = newAdjDict[src]
        for destele in neighbours:
            addEdge(destele, src)

def reverseDFS():
    global count
    global adjDict
    global path
    global scc
    
    while len(stack) != 0:
        curVertex = stack.pop()
        path = []
        if not visited[curVertex]:
            count += 1
            DFSUpdateStack(curVertex)
            scc[count] = path

def main():
    #Construct the adjacency list
    global adjDict
    global visited
    global path
    global count
    global stack 

    vertCount = 10
    initializeDict(vertCount)

    addEdge(0,1)
    addEdge(1,2)
    addEdge(2,0)
    addEdge(2,3)
    addEdge(3,4)
    addEdge(4,5)
    addEdge(5,6)
    addEdge(6,4)
    addEdge(6,7)
    addEdge(4,7)

    print (f'\nCurrent adjacency list : {adjDict}')

    DFSUpdateStack(0)
    stack.append(0)

    print (f'\nDFSUpdateStack traversal: {path}')
    print (f'\nStack content : {stack}')
    
    #Reverse the links
    reverseAdjList(vertCount)
    print (f'\nCurrent adjacency list after reverse : {adjDict}')
    visited = [False] * vertCount

    reverseDFS()
    print (f'No of SCCs : {count}')
    print (f'SCCs : {scc}')

if __name__ == "__main__":
    main()



