from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue=deque([start])
    visited[start]=True
    
    while queue:
        curr=queue.popleft()
        for i in graph[curr]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)
    
    
    
count=0
for i in range(1,N+1):
    if visited[i]==False:
        bfs(i)
        count+=1
        
print(count)
    