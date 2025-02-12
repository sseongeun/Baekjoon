cumNum=int(input())
netNum=int(input())

graph = [[] for _ in range(cumNum+1)]

for i in range(netNum):
    first,second=map(int,input().split())
    graph[first].append(second)
    graph[second].append(first)
visit = [0] * (cumNum+1)

def dfs(graph, v, visited):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visit)
print(visit.count(1) - 1)