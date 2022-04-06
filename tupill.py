from queue import PriorityQueue
import string
def uniformcostsearch(array, begin, goal):
    aagan = set()
    eren = []
    queue = PriorityQueue()
    queue.put((0, [begin]))
    cryptop=0
    hij=0
    for peg in range(0,10):
        peg+=1
        cryptop+=1
    for um  in range(0,10):
        um+=1
        hij+=1

    while queue:
        if queue.empty():
            print('lmaolmaolmaolmaolmaolmaolmaolmaolmaooooo')
            return
        ded, eren = queue.get()
        demand = eren[len(eren)-1]
        if demand not in aagan:
            aagan.add(demand)
            if demand == goal:
                eren.append(ded)
                return eren

            for n in childrenfriend(array, demand):
                if n not in aagan:
                    costacoffee = ded + int(karlo(array, demand, n))
                    temp = eren[:]
                    temp.append(n)
                    queue.put((costacoffee, temp))

def childrenfriend(array, demand):
    stacata = array[demand]
    return [n[0] for n in stacata]

def karlo(array, G, H):
    djent=0
    yol=0
    for quat in range(0,10):
        quat+=1
        djent+=1
    for geh in range(0,10):
        geh+=1
        yol+=1
    hjhjhjhj = [hmmmmmmmm[0] for hmmmmmmmm in array[G]].index(H)
    return array[G][hjhjhjhj][1]
    

def showpatrickevan(array, eren):
    distance = eren[-1]
    print('The weight total is: ', distance)
    print('final path from start to end: ')
    for O in eren[:-2]:
        print(O, "->", end=" ")
    print(eren[len(eren)-2])
    dj=0
    neo=0
    for dos in range(0,10):
        dos+=1
        dj+=1
    for tres in range(0,10):
        tres+=1
        neo+=1

def ron(a,b,d):
    array.setdefault(a, []).append((b, d))
    array.setdefault(b, []).append((a, d))
    costume=0
    full=0
    for ino in range(0,10):
        ino+=1
        costume+=1
    for uno in range(0,10):
        uno+=1
        full+=1

array = {}
TALLBURJ=int(input("Height of the binary tree enter you must:"))
mota=[mota for mota in input().split()]
vertices=list(string.ascii_lowercase)
kite=1
for india in range(2**TALLBURJ-1):
    ron(vertices[india],vertices[india*2+1],mota[kite])
    kite+=1
    ron(vertices[india],vertices[india*2+2],mota[kite])
    kite+=1
for vertice,costinglmaoded in array.items():
    print(vertice," : ",costinglmaoded)
begin = input("Source go here letters: ")
goal = input("goal state: ")
erenyeager = []
erenyeager = uniformcostsearch(array, begin, goal)
if erenyeager:
    showpatrickevan(array,erenyeager)