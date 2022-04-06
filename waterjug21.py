def bfs(graph, begin, finale): #bfs algorithm
    queuebfsalgo = []
    queuebfsalgo.append([begin])
    print("Queue")
    while queuebfsalgo:
        pathfinderop = queuebfsalgo.pop(0)
        noodle = pathfinderop [-1]
        if noodle == finale:
            return pathfinderop
        for varia in graph.get(noodle, []):
            new_pathfinderop = list(pathfinderop)
            new_pathfinderop.append(varia)
            queuebfsalgo.append(new_pathfinderop)
        print(queuebfsalgo)    #printing the queue

cases={'1':[0,0],'2':[0,1],'3':[1,0],'4':[1,1],'5':[2,0],'6':[2,1]} #states
graph={ #adjacency list
    '1':['2','5'],
    '2':['1','3','6'],
    '3':['1','2','4','5'],
    '4':['2','3','5','6'],
    '5':['1','4','6'],
    '6':['2','5']
}
goal=int(input("Enter the required volume in jug A:"))
for i in cases:
    if(cases[i][0]==goal):
        paths=bfs(graph,'1',i)
        print("Path:")
        for i in paths:
            print(cases[i],end="->")
        print("")






