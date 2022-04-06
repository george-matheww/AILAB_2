def add_edge(adj, src, dest): #for initialising adjacency matrix
    if (src==dest): #for disconnected vertice
        adj[src].append(dest)
    else:
        adj[src].append(dest)
        adj[dest].append(src)

def BFS(adj, src, dest, v, pred, dist): #BFS Algorithm
    queue = []
    visited = [False for i in range(v)]
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1
    visited[src] = True
    dist[src] = 0
    queue.append(src)
    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
                if (adj[u][i] == dest):
                    return True
    return False

def printShortestDistance(adj, s, dest, v): #finding shortest distance between the source and destination
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
  
    if (BFS(adj, s, dest, v, pred, dist) == False): #returns -1 if source and destination are disconnected
        print("-1")
        return
    path = []
    crawl = dest
    crawl = dest
    path.append(crawl)
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
    print("\nPath is : : ")
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=' ')

V=int(input("enter no. of cities")) #inputting the number of cities/vertices
adj = [[] for i in range(V)] #declaring the adjacency matrix
while(True):
    Lister=input().split()
    if(Lister[0]=="x"): #condition to stop taking inputs
        break
    add_edge(adj,int(Lister[0]),int(Lister[1]))
print(adj)
u=input("enter the source:")
vo=input("input destination:")
printShortestDistance(adj, int(u), int(vo), V)
