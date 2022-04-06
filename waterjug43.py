def bfs(graph, begin, finale): #bfs algorithm
    queuebfsalgo = []
    queuebfsalgo.append([begin])
    #print("Queue")
    while queuebfsalgo:
        pathfinderop = queuebfsalgo.pop(0)
        noodle = pathfinderop [-1]
        if noodle == finale:
            return pathfinderop
        for varia in graph.get(noodle, []):
            new_pathfinderop = list(pathfinderop)
            new_pathfinderop.append(varia)
            queuebfsalgo.append(new_pathfinderop)
        #print(queuebfsalgo)    #printing the queue

cases={'1':[0,0],'2':[4,0],'3':[0,3],'4':[4,3],'5':[1,3],'6':[3,0],'7':[1,0],
        '8':[3,3],'9':[0,1],'10':[4,2],'11':[4,1],'12':[0,2],'13':[2,3],'14':[2,0]} #states
graph={ #adjacency list
    '1':['2','3'],
    '2':['1','4','5'],
    '3':['1','4','6'],
    '4':['2','3'],
    '5':['2','3','4','7'],
    '6':['1','2','3','8'],
    '7':['1','2','5','9'],
    '8':['3','4','6','10'],
    '9':['1','3','7','11'],
    '10':['2','4','8','12'],
    '11':['2','4','9','13'],
    '12':['1','3','10','14'],
    '13':['3','4','11','14'],
    '14':['1','2','12','13']
}
goal=int(input("Enter the required volume in jug A:"))
for i in cases:
    if(cases[i][0]==goal):
        paths=bfs(graph,'1',i)
        print("Path:")
        for i in paths:
            print(cases[i],end="->")
        print("")






