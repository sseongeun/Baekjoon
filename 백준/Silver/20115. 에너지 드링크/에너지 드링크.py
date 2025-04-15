from collections import deque

N=int(input())
brinks = list(map(int,input().split()))

brinks.sort(reverse=True)
brinks=deque(brinks)

while len(brinks)!=1:
    first = brinks.popleft()
    second = brinks.popleft()
    brinks.appendleft(first+second/2)
    
if brinks[0].is_integer():
    print(int(brinks[0]))
else: 
    print(brinks[0])