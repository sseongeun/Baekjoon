import sys
input = sys.stdin.readline

T=int(input())

graph=[[0 for _ in range(31)] for _ in range(31)]

for i in range(1,31):
    graph[1][i]=i

for i in range(1,30):
    for j in range(i,30):
        for k in range(1,j):
            graph[i][j]+=graph[i-1][k]
            
for _ in range(T):
    a,b=map(int,input().split())
    print(graph[a][b])
        