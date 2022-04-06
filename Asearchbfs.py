def copypath(path):
  new_path=[]
  new_path.append(path[0])
  new_path.append([])
  for i in path[1]:
    new_path[1].append(i)
  return new_path

def Aboi(adj_matrix, begin, finale, n):
  priorityqueue=[[heur[begin-1],[begin-1]]]
  while(priorityqueue):
    priorityqueue.sort()
    pathfinderop=priorityqueue.pop(0)
    noodle=pathfinderop[1][-1]
    if(noodle==finale-1):
      return pathfinderop[::-1]
    else:
      for i in range(0,n):
        if(adj_matrix[noodle][i]!=0):
          temp_pathfinderop=copypath(pathfinderop)
          temp_pathfinderop[1].append(i)
          temp_pathfinderop[0]+=adj_matrix[noodle][i]+heur[i]
          priorityqueue.append(temp_pathfinderop)

def bfsboi(adj_matrix, begin, finale, n, heur):
  priorityqueue=[[heur[begin-1],[begin-1]]]
  while(priorityqueue):
    priorityqueue.sort()
    pathfinderop=priorityqueue.pop(0)
    noodle=pathfinderop[1][-1]
    if(noodle==finale-1):
      return pathfinderop[::-1]
    else:
      for i in range(0,n):
        if(adj_matrix[noodle][i]!=0):
          temp_pathfinderop=copypath(pathfinderop)
          temp_pathfinderop[1].append(i)
          temp_pathfinderop[0]+=adj_matrix[noodle][i]+heur[i]
          priorityqueue.append(temp_pathfinderop)
          
def bfs(graph, begin, finale): #bfs algorithm
    queuebfsalgo = []
    queuebfsalgo.append([0,[begin]])
    #print("Queue")
    while queuebfsalgo:
      queuebfsalgo.sort()
      pathfinderop = queuebfsalgo.pop(0)
      noodle = pathfinderop[1][-1]
      if noodle == finale:
        return pathfinderop
      for varia in graph.get(noodle, []):
        new_pathfinderop = copypath(pathfinderop)
        new_pathfinderop[1].append(varia)
        queuebfsalgo.append(new_pathfinderop)


n=int(input())
adj_matrix=[]
for i in range(n):
  adj_matrix.append(input().split())
  for j in range(len(adj_matrix[i])):
    adj_matrix[i][j]=int(adj_matrix[i][j])
heur=input().split()
for i in range(len(heur)):
    heur[i]=int(heur[i])
begin=int(input())
finale=int(input())

Aboipath=Aboi(adj_matrix,begin,finale, n)
Aboipath=Aboi(adj_matrix,begin,finale, n)
c1=Aboipath[1]
print(c1)
bfsboipath=bfsboi(adj_matrix,begin,finale, n, heur)
bfsboipath=bfsboi(adj_matrix,begin,finale, n, heur)
c2=bfsboipath[1]
for i in bfsboipath[0]:
  c2-=heur[i]
print(c2)
print(c1-c2)