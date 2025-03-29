def bfs(graph,start,visited):
    queue=[]
    queue.append(start)
    visited[start]=True
    
    while queue:
        curr=queue.pop()
        
        for neighbor in graph[curr]:
            if visited[neighbor]==False:
                queue.append(neighbor)
                visited[neighbor]=True
    



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
            bfs(graph,i,visited)
            cnt+=1
        
    return cnt