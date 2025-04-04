from collections import deque

T= int(input())

for _ in range(T):
    N,M=map(int,input().split())
    queue=deque(list(map(int,input().split())))
    
    max_num = max(queue)
    cnt=0
    
    while queue:
        if M==0:
            if queue[M] == max_num:
                queue.popleft()
                cnt+=1
                break
            else:
                queue.append(queue.popleft())
                M=len(queue)-1
        else:
            if queue[0] == max_num:
                queue.popleft()
                max_num = max(queue)
                cnt+=1
                M-=1
            else:
                queue.append(queue.popleft())
                M-=1
     
    print(cnt)           
    queue=[]
    cnt=0
    