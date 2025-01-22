import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx=[0,0,1,-1,1,1,-1,-1]
    dy=[-1,1,0,0,1,-1,1,-1]
    
    if x<0 or x>=M or y<0 or y>=N:
        return
    
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
            
N,M=map(int,input().split()) 
while N!=0 and M!=0:
    graph=[]
    for i in range(M):
        graph.append(list(map(int,input().split())))
        
    count=0       
    for i in range(M):
        for j in range(N):
            if graph[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)
    N,M=map(int,input().split()) 

 
        