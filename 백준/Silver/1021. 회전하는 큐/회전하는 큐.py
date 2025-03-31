from collections import deque

N,M=map(int,input().split())
nums = list(map(int,input().split()))

queue=deque([i for i in range(1,N+1)])
total_cnt = 0


for num in nums:
    curr_len = len(queue)
    cnt = 0
    
    while queue[0] != num:
        queue.appendleft(queue.pop())
        cnt+=1
        
    total_cnt += min(cnt, curr_len-cnt)
    queue.popleft()
    
print(total_cnt)