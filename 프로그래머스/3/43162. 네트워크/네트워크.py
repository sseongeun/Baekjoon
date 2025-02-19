from collections import deque

def dfs(curr,computers,n,visited):
    visited[curr]=True
    for i in range(n):
        if visited[i]==False and computers[curr][i]==1:
            dfs(i,computers,n,visited)    
        
    
def solution(n, computers):
    count=0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfs(i,computers,n,visited)
            count+=1

    return count
