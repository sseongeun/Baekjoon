n=int(input())
a,b=map(int,input().split()) # 두 사람의 촌수 (시작점, 도착점)
m=int(input())

graph=[[]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y= map(int,input().split()) #부모,자식
    graph[x].append(y)
    graph[y].append(x)
        
flag=False

def dfs(curr,count):
    global flag
    visited[curr]=True
    if curr==b: # 목표 노드에 도달한 경우
        print(count) # 현재 촌수 출력하기
        flag=True
    for i in graph[curr]:
        if visited[i]==False:
            dfs(i,count+1)
                
                
dfs(a,0)
if flag==False:
    print("-1")
