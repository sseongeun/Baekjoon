from collections import deque
import sys
input=sys.stdin.readline

dic={}

def dfs(graph,start):
    queue=deque()
    queue.append(start)
    dic[start]=0
    
    while queue:
        curr= queue.popleft()
        for neighbor in graph[curr]:
            if neighbor not in dic.keys():
                dic[neighbor]=dic[curr]+1
                queue.append(neighbor)
    

N,M,K,X=map(int,input().split()) # 도시개수, 도로개수, 거리, 출발도시 번호
graph= [[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b) # 방향 그래프니까 하나만 추가해줘야함
    

dfs(graph,X)
dic=dict(sorted(dic.items()))

has_value=False
for key,value in dic.items():
    if value == K:
        print(key)
        has_value=True
        
if has_value==False:
    print("-1")
    