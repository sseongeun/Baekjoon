import sys
sys.setrecursionlimit(10**6)

n=int(input())
nodes=[[] for _ in range(n+1)]

for _ in range(n-1):
    n1,n2,w=map(int,input().split())
    nodes[n1].append([n2,w])
    nodes[n2].append([n1,w])
    

def dfs(nodes,visited,start_node,curr_sum):
    global max_num, max_node
    
    visited[start_node]=True
    
    for neighbor in nodes[start_node]:
        if not visited[neighbor[0]]:
            if neighbor[1]+curr_sum>max_num:
                max_num=neighbor[1]+curr_sum
                max_node=neighbor[0]
            dfs(nodes,visited,neighbor[0],neighbor[1]+curr_sum)
                    
max_num=0
max_node=0
visited=[False]*(n+1)
dfs(nodes,visited,1,0)

visited=[False]*(n+1)
max_num=0
dfs(nodes,visited,max_node,0)

print(max_num)