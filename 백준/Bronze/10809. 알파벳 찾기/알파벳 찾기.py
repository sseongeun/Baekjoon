n=list(input())
nums=[[] for _ in range(26)]
a=ord("a")

for i in range(len(n)):
    nums[ord(n[i])-a].append(i)
    
for i in nums:
    if len(i)==0:
        print("-1",end=" ")
    else:
        print(min(i),end=" ")