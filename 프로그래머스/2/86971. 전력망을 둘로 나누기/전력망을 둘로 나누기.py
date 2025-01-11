from collections import deque

def bfs(graph,start,visited):
    total=1
    queue=deque()
    queue.append(start)
    visited[start]=True
    
    while queue:
        curr = queue.popleft()

        
        for i in graph[curr]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                total+=1
    return total
    

def makeGraph(wires,n):
    graph=[[] for _ in range(n+1)]

    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        graph[i[0]]=list(set(graph[i[0]]))
        graph[i[1]]=list(set(graph[i[1]]))
    return graph
    


def solution(n, wires):
    
    result=[]

    # 새로운 그래프를 만드는 방법
    for i in range(len(wires)): # 특정 간선이 제거될때마다 절대값의 차를 구한다.
        tempWires = wires[:]
        tempWires.pop(i)
        newGraph=makeGraph(tempWires,n)

        visited = [False]*(n+1)
        routeLen = bfs(newGraph,1,visited)
        result.append(abs(routeLen-(n-routeLen)))


    return min(result)