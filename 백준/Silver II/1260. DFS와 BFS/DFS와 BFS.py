from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
N,M,v=map(int,input().split())
v2=v
graph=[[],]
for i in range(N):
    graph.append([])

for j in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    

visited=[False]*(N+1)
dfs(graph,v,visited)
print( )
visited=[False]*(N+1)
bfs(graph,v2,visited)