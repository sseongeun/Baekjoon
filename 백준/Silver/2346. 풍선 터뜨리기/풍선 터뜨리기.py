import sys
from collections import deque

n=int(input())  
nums=deque(enumerate(map(int,input().split()),start=1)) 

for i in range(n):
    curr=nums.popleft()
    print(curr[0],end=" ")
    if curr[1]>0:
        nums.rotate(-(curr[1]-1))
    else:
        nums.rotate(-curr[1])