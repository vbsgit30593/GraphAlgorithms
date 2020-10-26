#global variables
adjDict = {}
visited = []
path = list()
queue = list()
count = 0
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

def BFS():
    global adjDict
    global path
    global visited
    global queue
    global count

    count += 1
    if (len(queue)):
        queueFirst = queue.pop(0)
        if not visited[queueFirst]:
            visited[queueFirst] = True
            path.append(queueFirst)

        for ele in adjDict[queueFirst]:
            if not visited[ele]:
                visited[ele] = True
                queue.append(ele)
                path.append(ele)

        BFS()        


def main():
    #Construct the adjacency list
    global adjDict
    global visited
    global path
    global queue
    global count

    vertCount = 10
    initializeDict(vertCount)
    addEdge(0,1);
    addEdge(0,3);
    addEdge(1,0);
    addEdge(1,2);
    addEdge(1,4);
    addEdge(1,6);
    addEdge(1,7);
    addEdge(2,1);
    addEdge(2,3);
    addEdge(2,8);
    addEdge(2,9);
    addEdge(3,0);
    addEdge(3,2);
    addEdge(4,1);
    addEdge(4,5);
    addEdge(4,6);
    addEdge(4,7);
    addEdge(5,4);
    addEdge(6,1);
    addEdge(6,4);
    addEdge(6,7);
    addEdge(7,1);
    addEdge(7,4);
    addEdge(7,6);
    addEdge(8,2);
    addEdge(9,2);

    print (f'\nCurrent adjacency list : {adjDict}')
    queue.append(0)
    BFS()

    print (f'\nBFS traversal: {path}')
    print(count)

if __name__ == "__main__":
    main()



