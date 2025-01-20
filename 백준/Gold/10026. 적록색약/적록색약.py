import sys
import copy
sys.setrecursionlimit(10**6)

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(input()))
    
first_graph=copy.deepcopy(graph)
second_graph=copy.deepcopy(graph)

def dfs(graph,x,y,color):
    if x<0 or x>=N or y<0 or y>=N or graph[x][y]!=color:
        return
    
    graph[x][y]='#'
    
    dfs(graph,x-1,y,color)
    dfs(graph,x+1,y,color)
    dfs(graph,x,y-1,color)
    dfs(graph,x,y+1,color)
    
    
def count_groups(graph):
    rc,bc,gc=0,0,0
    for i in range(N):
        for j in range(N):
            if graph[i][j]=="R":
                dfs(graph,i,j,"R")
                rc+=1
            elif graph[i][j]=="B":
                dfs(graph,i,j,"B")
                bc+=1
            elif graph[i][j]=="G":
                dfs(graph,i,j,"G")
                gc+=1
    return rc,bc,gc


r,b,c=count_groups(first_graph)

for i in range(N):
    for j in range(N):
        if second_graph[i][j]=='R':
            second_graph[i][j]='G'

r2,b2,c2=count_groups(second_graph)

print(r+b+c,c2+b2)
           