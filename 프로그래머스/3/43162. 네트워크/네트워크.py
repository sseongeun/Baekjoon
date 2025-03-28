def dfs(visited,graph,curr):
    queue=[]
    queue.append(curr)
    visited[curr]=True
    
    while queue:
        curr = queue.pop()
        
        for neighbors in graph[curr]:
            if visited[neighbors]==False:
                queue.append(neighbors)
                visited[neighbors]=True
    

def solution(n, computers):
    graph=[[] for _ in range(n)]
    visited=[False]*n

    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
                graph[i]=list(set(graph[i]))
                graph[j]=list(set(graph[j]))

    cnt=0           
    for i in range(n):
        if visited[i]==False:
            dfs(visited,graph,i)
            cnt+=1

    return cnt
