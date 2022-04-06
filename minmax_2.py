import math
def minimax(arr,zero):
    for i in range(zero-1,-1,-1):
        if(i>=3 and i<=6):
            arr[i]=max(arr[(i*2)+1],arr[(i*2)+2])
        elif(i>=1 and i<=2):
            arr[i]=min(arr[(i*2)+1],arr[(i*2)+2])
        else:
            arr[i]=max(arr[(i*2)+1],arr[(i*2)+2])
    print("the final tree is:",arr)
depth=int(input("input the depth:"))
treesize=(2**(depth+1))-1
scores=list(map(int,input().split()))
tree=[]
counter=0
zeroes = (2**depth)-1
for j in range(0,zeroes):
    tree.append(0)
for k in scores:
    tree.append(k)
minimax(tree,zeroes)

#scores = [-1,-1,0,1,1,-1,1,1]

#print("The optimal value is : ", end = "")
#print(minimax(0, 0, True, scores,depth))