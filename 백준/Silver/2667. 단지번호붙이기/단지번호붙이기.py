N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input())))

count=0
def dfs(x,y):
    global count 
    
    if x<0 or x>=N or y<0 or y>=N:
        return
    
    if graph[x][y]==1:
        graph[x][y]=0
        count+=1
            
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    
    
result=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(count)
            count=0
            
print(len(result))
result.sort()
for i in result:
    print(i)