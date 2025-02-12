from collections import deque

N,M=map(int,input().split())
result=-1

q=deque()
q.append((N,1))

while q:
    curr,h=q.popleft()

    if curr==M:
        result=h
        break
    
    if curr*2<=M:
        q.append((curr*2,h+1))

    if curr*10+1<=M:
        q.append((curr*10+1,h+1))
    
print(result)