N= int(input()) # 집의 개수
graph = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(3):
        if j==0:
            graph[i][j]+=min(graph[i-1][1], graph[i-1][2])
        elif j==1:
            graph[i][j]+=min(graph[i-1][0], graph[i-1][2])
        else:
            graph[i][j]+=min(graph[i-1][0], graph[i-1][1])

print(min(graph[N-1]))