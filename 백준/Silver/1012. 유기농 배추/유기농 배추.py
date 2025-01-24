import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T=int(input())
    
for i in range(T):
    M,N,B=map(int,input().split())  # 가로, 세로
    graph=[[0]*M for _ in range(N)]
    for _ in range(B):
        a,b=map(int,input().split())
        graph[b][a]=1
        
    def dfs(x,y):
        if x<0 or x>=N or y<0 or y>=M:
            return
        if graph[x][y]==1:
            graph[x][y]=0
            
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
        
    count=0 
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                dfs(i,j)
                count+=1
                
    print(count)