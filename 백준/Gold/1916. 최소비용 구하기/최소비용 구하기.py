import heapq
import sys
input=sys.stdin.readline

INF=int(1e9)

N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
distance=[INF]*(N+1)

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
    
def dijakstra(start,graph):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now= heapq.heappop(q)
        
        if dist>distance[now]:
            continue
        
        for i in graph[now]:
            cost= dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
 
start,end=map(int,input().split())               
dijakstra(start,graph)
print(distance[end])
        