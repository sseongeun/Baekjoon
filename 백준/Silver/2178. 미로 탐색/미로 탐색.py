from collections import deque


row,col=map(int,input().split())
graph=[]
for i in range(row):
    graph.append(list(map(int,input())))
    
def dns(graph,row,col):
    queue=deque()
    queue.append((0,0))
    
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=row or ny<0 or ny>=col:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
        
    return graph[-1][-1]



print(dns(graph,row,col))