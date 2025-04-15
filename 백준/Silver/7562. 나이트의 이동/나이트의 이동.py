from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph,start,end,N):
    if start == end :
        return 0
    
    dx=[-2,-1,1,2,-2,-1,1,2]
    dy=[1,2,2,1,-1,-2,-2,-1]
    
    queue=deque()
    queue.append((start[0],start[1]))
    
    while queue:
        x,y= queue.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==0:
                graph[nx][ny]= graph[x][y]+1
                queue.append((nx,ny))
                if nx==end[0] and ny==end[1]:
                    return graph[nx][ny]
                

T=int(input())
for _ in range(T):
    N=int(input())
    graph=[[0 for _ in range(N)] for _ in range(N)]
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    print(dfs(graph,start,end,N))
