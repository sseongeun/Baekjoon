from itertools import combinations

N,S=map(int,input().split())
nums=list(map(int,input().split()))
comb=[]
cnt=0  
    
for i in range(1,N+1):
    comb=combinations(nums,i)
     
    for c in comb:
        if sum(list(c))==S:
            cnt+=1

print(cnt)