N,M=map(int,input().split()) # 세로, 가로   
graph=[list(map(int, input().strip())) for _ in range(N)]

    
max_size = 1
     
    
for i in range(N):
    for j in range(M):
        for size in range(1, min(N,M)):
            if i+size<N and j+size<M:
                if graph[i][j]== graph[i][j+size]== graph[i+size][j]== graph[i+size][j+size]:
                    max_size=max(max_size,size+1)
                    
print(max_size**2)