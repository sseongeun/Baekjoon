import math

def dfs(start,graph,n):
    visited=[False]*(n+1)
    queue=[]
    cnt=1
    queue.append(start)
    visited[start]=True
    
    while queue:
        curr= queue.pop()
        for neighbor in graph[curr]:
            if visited[neighbor]== False:
                visited[neighbor]=True
                queue.append(neighbor)
                cnt+=1
    return cnt

def make_graph(wires,n):    
    graph=[[] for _ in range(n+1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        graph[wire[0]]= list(set(graph[wire[0]]))
        graph[wire[1]]= list(set(graph[wire[1]]))
        
    return graph

def solution(n, wires):
    result=[]

    for wire in wires:
        temp=wires.copy()
        temp.remove(wire)

        new_graph = make_graph(temp,n)

        cnt1=dfs(wire[0],new_graph,n)
        cnt2=dfs(wire[1],new_graph,n)

        result.append(abs(cnt1-cnt2))

    return min(result)
