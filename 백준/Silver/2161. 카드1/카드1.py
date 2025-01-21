from collections import deque

N=int(input())
num=[i for i in range(1,N+1)]

queue=deque(num)
answer=[]

while queue:
    answer.append(queue.popleft())
    if len(queue)!=0:
     queue.append(queue.popleft())
    
print(*answer)