from itertools import product

N,M=map(int,input().split())
nums=list(map(int,input().split()))
result=[]

for i in product(nums,repeat=M):
    result.append(i)
  
result.sort(reverse=False)
for i in result:
    print(*i)