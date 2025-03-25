def dfs(computers,n,start,visited):
    if visited[start]==False:
        visited[start]=True
        for i in range(n):
            if computers[start][i]==1 and visited[i]== False:
                dfs(computers,n,i,visited)
    else:
        return

def solution(n, computers):
    visited=[False]*n
    cnt=0
    
    for i in range(n):
        if visited[i]==False:
            dfs(computers,n,i,visited)
            cnt+=1
    return cnt