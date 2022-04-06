from queue import PriorityQueue
def ucs(start, goal, graph):
    visited = set()
    queue = PriorityQueue()
    queue.put((graph[0], start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return
            norway=[]
            norway.append(graph[(2*node)+1])
            norway.append(graph[(2*node)+2])
            for neighbor in norway:
                if neighbor not in visited:
                    totalcost= cost + graph[node+neighbor]
                    queue.put((totalcost,neighbor))

h=int(input("enter height:"))
size=2**(h+1)-1
start=int(input("enter start node 0:"))
goal=int(input("enter goal node:"))
arr=[]
for i in range(0,size):
    ele=int(input())
    arr.append(ele)
ucs(start,goal,arr)

