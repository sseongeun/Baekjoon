N=int(input())
graph=[]
in_list=[[] for _ in range(N)]

    
for i in range(N):
    graph.append(list(map(int,input().split())))
    
for i in range(N): # 중간 노드 (무조건 중간 노드를 처음에 지정해야한다!!)
    for j in range(N): # 시작 노드
        for k in range(N): # 도착 노드
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
            
            
            
for row in graph:
    print(*row)
