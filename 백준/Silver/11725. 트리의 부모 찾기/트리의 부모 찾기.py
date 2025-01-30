from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
graph=[[]*(N+1)for _ in range(N+1)]

for i in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent=[0]*(N+1)
parent[1]=0

q=deque()
q.append(1)

while q:
    curr= q.popleft()
    for i in graph[curr]:
        if parent[i]==0:
            parent[i]=curr
            q.append(i)
            
for i in parent[2:]:
    print(i)