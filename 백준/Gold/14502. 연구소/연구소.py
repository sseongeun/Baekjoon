from itertools import combinations
from collections import deque
import copy

def bfs(graph,wall,virus):
    
    # 벽 세우기
    for w in wall:
        graph[w[0]][w[1]]=1

    # 바이러스 기준으로 바이러스 퍼뜨리기
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue = deque(virus)
    
    while queue:
        curr = queue.popleft()
        nx,ny = curr[0],curr[1]
        
        for i in range(4):
            if nx+dx[i]>=0 and nx+dx[i]<N and ny+dy[i]>=0 and ny+dy[i]<M:
                if graph[nx+dx[i]][ny+dy[i]]==0:
                    graph[nx+dx[i]][ny+dy[i]]=2
                    queue.append((nx+dx[i],ny+dy[i]))
                                
    return graph
    
    
      
# 입력 받기      
N,M = map(int,input().split()) # 세로, 가로
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
    
    
# 1) 벽을 세울 좌표 결정
walls=[]
verius=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            walls.append((i,j))
        elif graph[i][j]==2:
            verius.append((i,j))      

walls = list(combinations(walls,3)) # 벽을 세울 3개의 좌표
cnt_list=[]

for wall in walls:
    temp_graph = copy.deepcopy(graph)
    cnt=0
    temp_graph=bfs(temp_graph,wall,verius)
     
       
    for t in temp_graph:
        for ele in t:
            if ele == 0:
                cnt+=1
    cnt_list.append(cnt)
 
print(max(cnt_list))  
